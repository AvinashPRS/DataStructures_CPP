"""
Graph built from an adjacency matrix (0 = no edge), directed or undirected, with:
  traversal (BFS, DFS), connectivity, cycle detection, topological sort (Kahn & DFS),
  shortest paths (unweighted BFS, Dijkstra, Bellman-Ford, Floyd-Warshall),
  MST (Prim, Kruskal), bipartite check, articulation points and bridges.

NOTE: the C++ Graph.cpp in this folder did not compile against its own headers
(GraphEdge argument order / getIndex()); this Python version uses one consistent API.
"""
import heapq
import itertools
import sys
from collections import deque

from graph_edge import GraphEdge
from graph_node import GraphNode

INF = float("inf")


class Graph:
    # ================================================================
    # Constructor
    # ================================================================
    def __init__(self, number_of_vertices, adjacency_matrix, directed=False):
        self.adjacency_matrix = adjacency_matrix
        self.number_of_vertices = number_of_vertices
        self.directed = directed
        self.edges = []
        self.vertices = []
        self.adjacency_list = {}  # GraphNode -> list[GraphEdge]
        self.create_nodes()
        self.create_edges()
        self.create_adjacency_list()

    # ================================================================
    # CREATE NODES
    # ================================================================
    def create_nodes(self):
        for i in range(self.number_of_vertices):
            self.vertices.append(GraphNode(i))

    # ================================================================
    # CREATE EDGES FROM ADJACENCY MATRIX
    # Assumption: adjacency_matrix[i][j] == 0 means there is no edge.
    # For an undirected graph matrix[i][j] == matrix[j][i]; we create the edge only once.
    # ================================================================
    def create_edges(self):
        for i in range(self.number_of_vertices):
            for j in range(self.number_of_vertices):
                weight = self.adjacency_matrix[i][j]
                if weight == 0:  # No edge
                    continue
                # Undirected graph: matrix[0][1] = matrix[1][0] = 5 -> we want only ONE edge.
                if not self.directed and j <= i:
                    continue
                self.edges.append(GraphEdge(weight, self.vertices[i], self.vertices[j]))

    # ================================================================
    # CREATE ADJACENCY LIST: node -> list of all connected edges
    #
    #         5
    #     A ------- B          A -> AB, AC
    #     |                    B -> AB
    #   10|                    C -> AC
    #     C
    #
    # For directed graphs, only outgoing edges are inserted.
    # ================================================================
    def create_adjacency_list(self):
        self.adjacency_list = {node: [] for node in self.vertices}  # includes isolated vertices
        for edge in self.edges:
            self.adjacency_list[edge.get_node1()].append(edge)  # Outgoing edge from node1
            if not self.directed:  # For undirected graph, edge belongs to both endpoints.
                self.adjacency_list[edge.get_node2()].append(edge)

    # ================================================================
    # ADD NODE / ADD EDGE
    # ================================================================
    def add_node(self, index):
        node = GraphNode(index)
        self.vertices.append(node)
        self.adjacency_list[node] = []
        self.number_of_vertices += 1
        return node

    def add_edge(self, node1, node2, weight):
        if node1 is None or node2 is None:
            return None
        edge = GraphEdge(weight, node1, node2)
        self.edges.append(edge)
        self.adjacency_list[node1].append(edge)
        if not self.directed:
            self.adjacency_list[node2].append(edge)
        return edge

    # ================================================================
    # GETTERS
    # ================================================================
    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_adjacency_list(self):
        return self.adjacency_list

    # ================================================================
    # GET OTHER ENDPOINT OF AN UNDIRECTED EDGE
    #   edge = A -------- B :  get_other_node(edge, A) -> B,  get_other_node(edge, B) -> A
    # ================================================================
    @staticmethod
    def get_other_node(edge, node):
        if edge is None or node is None:
            return None
        if edge.get_node1() is node:
            return edge.get_node2()
        if edge.get_node2() is node:
            return edge.get_node1()
        return None

    def _neighbor(self, edge, node):
        # directed: adjacency list only contains outgoing edges
        return edge.get_node2() if self.directed else self.get_other_node(edge, node)

    # ================================================================
    # BFS  (queue)  Time: O(V + E)  Space: O(V)
    # ================================================================
    def bfs(self, start):
        result = []
        if start is None:
            return result
        visited = {start}  # Mark when inserting into queue.
        q = deque([start])
        while q:
            current = q.popleft()
            result.append(current.get_index())
            for edge in self.adjacency_list.get(current, []):
                nb = self._neighbor(edge, current)
                if nb is not None and nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        return result

    # ================================================================
    # DFS  Time: O(V + E)  Space: O(V)
    # ================================================================
    def _dfs_helper(self, node, visited, result):
        visited.add(node)
        result.append(node.get_index())
        for edge in self.adjacency_list.get(node, []):
            nb = self._neighbor(edge, node)
            if nb is not None and nb not in visited:
                self._dfs_helper(nb, visited, result)

    def dfs(self, start):
        result = []
        if start is None:
            return result
        self._dfs_helper(start, set(), result)
        return result

    # ================================================================
    # PATH EXISTS (BFS)  Time: O(V + E)
    # ================================================================
    def path_exists(self, source, destination):
        if source is None or destination is None:
            return False
        if source is destination:
            return True
        q = deque([source])
        visited = {source}
        while q:
            current = q.popleft()
            for edge in self.adjacency_list[current]:
                nb = self._neighbor(edge, current)
                if nb is None:
                    continue
                if nb is destination:
                    return True
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        return False

    # ================================================================
    # CONNECTED COMPONENTS  (intended for UNDIRECTED graphs)  Time: O(V + E)
    # ================================================================
    def connected_components(self):
        visited = set()
        count = 0
        for node in self.vertices:
            if node in visited:
                continue
            count += 1
            q = deque([node])
            visited.add(node)
            while q:
                current = q.popleft()
                for edge in self.adjacency_list[current]:
                    nb = self.get_other_node(edge, current)
                    if nb is not None and nb not in visited:
                        visited.add(nb)
                        q.append(nb)
        return count

    # ================================================================
    # UNDIRECTED CYCLE DETECTION
    # Seeing the parent again is NOT a cycle:   A - B   (DFS(B) sees A = its parent)
    # But in   A / \ B---C   if C sees A after coming from B, a cycle exists.
    # ================================================================
    def _cycle_undirected_dfs(self, node, parent, visited):
        visited.add(node)
        for edge in self.adjacency_list[node]:
            nb = self.get_other_node(edge, node)
            if nb is None:
                continue
            if nb not in visited:
                if self._cycle_undirected_dfs(nb, node, visited):
                    return True
            elif nb is not parent:
                return True
        return False

    def has_cycle_undirected(self):
        visited = set()
        for node in self.vertices:
            if node not in visited and self._cycle_undirected_dfs(node, None, visited):
                return True
        return False

    # ================================================================
    # DIRECTED CYCLE DETECTION
    # States: 0 = unvisited, 1 = in DFS recursion stack, 2 = completely processed.
    # Back edge (state[neighbor] == 1) indicates a cycle.
    # ================================================================
    def _cycle_directed_dfs(self, node, state):
        state[node] = 1
        for edge in self.adjacency_list[node]:
            nb = edge.get_node2()
            if nb is None:
                continue
            if state[nb] == 1:
                return True
            if state[nb] == 0 and self._cycle_directed_dfs(nb, state):
                return True
        state[node] = 2
        return False

    def has_cycle_directed(self):
        state = {node: 0 for node in self.vertices}
        for node in self.vertices:
            if state[node] == 0 and self._cycle_directed_dfs(node, state):
                return True
        return False

    # ================================================================
    # TOPOLOGICAL SORT - KAHN'S ALGORITHM (indegree + queue)
    # Valid only for a DAG. If len(result) != V, the graph contains a cycle -> [].
    # ================================================================
    def topological_sort_kahn(self):
        if not self.directed:
            return []
        indegree = {node: 0 for node in self.vertices}
        for edge in self.edges:
            indegree[edge.get_node2()] += 1
        q = deque(node for node in self.vertices if indegree[node] == 0)
        result = []
        while q:
            current = q.popleft()
            result.append(current.get_index())
            for edge in self.adjacency_list[current]:
                nb = edge.get_node2()
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        return result if len(result) == len(self.vertices) else []  # Cycle detected

    # ================================================================
    # TOPOLOGICAL SORT USING DFS (vertex is pushed AFTER all its descendants)
    # ================================================================
    def _topo_dfs(self, node, visited, stack):
        visited.add(node)
        for edge in self.adjacency_list[node]:
            nb = edge.get_node2()
            if nb not in visited:
                self._topo_dfs(nb, visited, stack)
        stack.append(node.get_index())

    def topological_sort_dfs(self):
        if not self.directed or self.has_cycle_directed():
            return []
        visited, stack = set(), []
        for node in self.vertices:
            if node not in visited:
                self._topo_dfs(node, visited, stack)
        return stack[::-1]

    # ================================================================
    # SHORTEST PATH IN AN UNWEIGHTED GRAPH
    # BFS guarantees shortest path when every edge has equal cost.
    # distance[source] = 0, unreachable vertex = INF
    # ================================================================
    def shortest_path_unweighted(self, source):
        distance = [INF] * self.number_of_vertices
        if source is None:
            return distance
        si = source.get_index()
        if si < 0 or si >= self.number_of_vertices:
            return distance
        distance[si] = 0
        q = deque([source])
        while q:
            current = q.popleft()
            ci = current.get_index()
            for edge in self.adjacency_list[current]:
                nb = self._neighbor(edge, current)
                if nb is None:
                    continue
                ni = nb.get_index()
                if distance[ni] == INF:
                    distance[ni] = distance[ci] + 1
                    q.append(nb)
        return distance

    # ================================================================
    # DIJKSTRA   Requirements: edge weights >= 0.  Min priority queue.  O((V + E) log V)
    # ================================================================
    def dijkstra(self, source):
        distance = [INF] * self.number_of_vertices
        if source is None:
            return distance
        distance[source.get_index()] = 0
        counter = itertools.count()  # tie-breaker so nodes are never compared
        pq = [(0, next(counter), source)]
        while pq:
            current_distance, _, current = heapq.heappop(pq)
            ci = current.get_index()
            # Ignore stale priority queue entry: earlier distance[A] = 10, later 5,
            # the queue can still contain (10, A).
            if current_distance > distance[ci]:
                continue
            for edge in self.adjacency_list[current]:
                w = edge.get_weight()
                if w < 0:  # Dijkstra cannot handle negative edges.
                    raise ValueError("Dijkstra cannot handle negative weights")
                nb = self._neighbor(edge, current)
                if nb is None:
                    continue
                ni = nb.get_index()
                nd = distance[ci] + w
                if nd < distance[ni]:
                    distance[ni] = nd
                    heapq.heappush(pq, (nd, next(counter), nb))
        return distance

    # ================================================================
    # BELLMAN-FORD   Supports negative-weight edges, detects negative cycles.  O(VE)
    # ================================================================
    def bellman_ford(self, source):
        distance = [INF] * self.number_of_vertices
        if source is None:
            return distance
        distance[source.get_index()] = 0

        # Relax all edges V - 1 times.
        for _ in range(1, self.number_of_vertices):
            changed = False
            for edge in self.edges:
                u, v, w = edge.get_node1().get_index(), edge.get_node2().get_index(), edge.get_weight()
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    changed = True
                # An undirected edge can be relaxed in both directions.
                if not self.directed and distance[v] + w < distance[u]:
                    distance[u] = distance[v] + w
                    changed = True
            # Optimization: if nothing changed, shortest distances are already final.
            if not changed:
                break

        # Negative cycle detection
        for edge in self.edges:
            u, v, w = edge.get_node1().get_index(), edge.get_node2().get_index(), edge.get_weight()
            if distance[u] + w < distance[v] or (not self.directed and distance[v] + w < distance[u]):
                raise RuntimeError("Negative-weight cycle detected")
        return distance

    # ================================================================
    # FLOYD-WARSHALL   Shortest path between EVERY pair.  Time O(V^3), Space O(V^2)
    # dist[i][j] = min(old path i -> j, i -> k -> j) for each intermediate vertex k
    # ================================================================
    def floyd_warshall(self):
        n = self.number_of_vertices
        distance = [[INF] * n for _ in range(n)]
        for i in range(n):  # Distance from vertex to itself
            distance[i][i] = 0
        for edge in self.edges:  # Add graph edges
            u, v, w = edge.get_node1().get_index(), edge.get_node2().get_index(), edge.get_weight()
            distance[u][v] = min(distance[u][v], w)
            if not self.directed:
                distance[v][u] = min(distance[v][u], w)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
        return distance

    # ================================================================
    # PRIM MST   Valid for weighted undirected graphs.  O(E log E) ~ O(E log V)
    # ================================================================
    def prim_mst(self, start):
        mst = []
        if self.directed or start is None:
            return mst
        visited = {start}
        counter = itertools.count()
        pq = []
        for edge in self.adjacency_list[start]:
            heapq.heappush(pq, (edge.get_weight(), next(counter), edge))
        while pq and len(mst) < len(self.vertices) - 1:
            _, _, edge = heapq.heappop(pq)
            n1, n2 = edge.get_node1(), edge.get_node2()
            v1, v2 = n1 in visited, n2 in visited
            # Both endpoints already inside MST; adding this edge would create a cycle.
            if v1 and v2:
                continue
            nxt = n2 if v1 else n1
            mst.append(edge)
            visited.add(nxt)
            for e in self.adjacency_list[nxt]:
                other = self.get_other_node(e, nxt)
                if other is not None and other not in visited:
                    heapq.heappush(pq, (e.get_weight(), next(counter), e))
        return mst

    # ================================================================
    # KRUSKAL MST   Disjoint Set Union (Union-Find).  Sorting = O(E log E);
    # DSU operations are almost constant time.
    # ================================================================
    def kruskal_mst(self):
        mst = []
        if self.directed:
            return mst
        sorted_edges = sorted(self.edges, key=lambda e: e.get_weight())
        parent = list(range(self.number_of_vertices))
        rank = [0] * self.number_of_vertices

        def find_set(node):  # FIND with path compression
            if parent[node] != node:
                parent[node] = find_set(parent[node])
            return parent[node]

        def union_sets(a, b):  # UNION by rank
            ra, rb = find_set(a), find_set(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        for edge in sorted_edges:
            if union_sets(edge.get_node1().get_index(), edge.get_node2().get_index()):
                mst.append(edge)
                if len(mst) == len(self.vertices) - 1:
                    break
        return mst

    # ================================================================
    # BIPARTITE GRAPH  (2-color BFS)
    # color: -1 = not colored, 0 = first color, 1 = second color.
    # Adjacent vertices must have different colors.  Time: O(V + E)
    # ================================================================
    def is_bipartite(self):
        if self.directed:
            return False  # treated as an undirected graph property
        color = [-1] * self.number_of_vertices
        for start in self.vertices:
            si = start.get_index()
            if color[si] != -1:
                continue
            color[si] = 0
            q = deque([start])
            while q:
                current = q.popleft()
                ci = current.get_index()
                for edge in self.adjacency_list[current]:
                    nb = self.get_other_node(edge, current)
                    if nb is None:
                        continue
                    ni = nb.get_index()
                    if color[ni] == -1:
                        color[ni] = 1 - color[ci]
                        q.append(nb)
                    elif color[ni] == color[ci]:
                        return False
        return True

    # ================================================================
    # ARTICULATION POINTS
    # discovery[node]: DFS discovery time
    # low[node]: earliest discovery time reachable through subtree/back edge.
    # A non-root vertex u is an articulation point if low[v] >= discovery[u] for a DFS child v.
    # The root is an articulation point if it has > 1 DFS children.
    # ================================================================
    def _articulation_dfs(self, node, parent, timer, discovery, low, visited, result):
        visited.add(node)
        discovery[node] = low[node] = timer[0]
        timer[0] += 1
        children = 0
        for edge in self.adjacency_list[node]:
            nb = self.get_other_node(edge, node)
            if nb is None or nb is parent:
                continue
            if nb not in visited:
                children += 1
                self._articulation_dfs(nb, node, timer, discovery, low, visited, result)
                low[node] = min(low[node], low[nb])
                if parent is not None and low[nb] >= discovery[node]:  # Non-root articulation
                    result.add(node.get_index())
            else:
                low[node] = min(low[node], discovery[nb])  # Back edge
        if parent is None and children > 1:  # Root articulation point
            result.add(node.get_index())

    def articulation_points(self):
        if self.directed:
            return []
        discovery, low, visited, points = {}, {}, set(), set()
        timer = [0]  # boxed int so recursion can mutate it (C++ used int&)
        for node in self.vertices:
            if node not in visited:
                self._articulation_dfs(node, None, timer, discovery, low, visited, points)
        return sorted(points)

    # ================================================================
    # BRIDGES
    # Edge u-v is a bridge if low[v] > discovery[u]: v's subtree cannot reach u or any
    # ancestor of u without using edge u-v.
    # ================================================================
    def _bridge_dfs(self, node, parent, timer, discovery, low, visited, result):
        visited.add(node)
        discovery[node] = low[node] = timer[0]
        timer[0] += 1
        for edge in self.adjacency_list[node]:
            nb = self.get_other_node(edge, node)
            if nb is None or nb is parent:
                continue
            if nb not in visited:
                self._bridge_dfs(nb, node, timer, discovery, low, visited, result)
                low[node] = min(low[node], low[nb])
                if low[nb] > discovery[node]:
                    result.append((node.get_index(), nb.get_index()))
            else:
                low[node] = min(low[node], discovery[nb])

    def bridges(self):
        if self.directed:
            return []
        discovery, low, visited, result = {}, {}, set(), []
        timer = [0]
        for node in self.vertices:
            if node not in visited:
                self._bridge_dfs(node, None, timer, discovery, low, visited, result)
        return result


def _fmt(dist):
    return ["INF" if d == INF else d for d in dist]


# demo harness (the C++ folder had no main for this Graph):
if __name__ == "__main__":
    sys.setrecursionlimit(10000)

    #  Undirected weighted graph:
    #     0 --4-- 1 --2-- 2
    #     |       |
    #     1       5
    #     |       |
    #     3 --3-- 4      5 (isolated)
    m = [[0] * 6 for _ in range(6)]
    for u, v, w in [(0, 1, 4), (1, 2, 2), (0, 3, 1), (1, 4, 5), (3, 4, 3)]:
        m[u][v] = m[v][u] = w
    g = Graph(6, m)
    v = g.get_vertices()
    print("BFS from 0:", g.bfs(v[0]))
    print("DFS from 0:", g.dfs(v[0]))
    print("Path 0->2 exists:", g.path_exists(v[0], v[2]), "| 0->5:", g.path_exists(v[0], v[5]))
    print("Connected components:", g.connected_components())
    print("Has cycle (undirected):", g.has_cycle_undirected())
    print("Unweighted distances from 0:", _fmt(g.shortest_path_unweighted(v[0])))
    print("Dijkstra from 0:", _fmt(g.dijkstra(v[0])))
    print("Bellman-Ford from 0:", _fmt(g.bellman_ford(v[0])))
    print("Floyd-Warshall row 0:", _fmt(g.floyd_warshall()[0]))
    print("Prim MST:", g.prim_mst(v[0]), "weight =", sum(e.get_weight() for e in g.prim_mst(v[0])))
    print("Kruskal MST:", g.kruskal_mst(), "weight =", sum(e.get_weight() for e in g.kruskal_mst()))
    print("Bipartite:", g.is_bipartite())
    print("Articulation points:", g.articulation_points())
    print("Bridges:", g.bridges())

    # Directed acyclic graph: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1
    dm = [[0] * 6 for _ in range(6)]
    for u, w in [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]:
        dm[u][w] = 1
    dg = Graph(6, dm, directed=True)
    print("\nDirected: has cycle:", dg.has_cycle_directed())
    print("Topological sort (Kahn):", dg.topological_sort_kahn())
    print("Topological sort (DFS): ", dg.topological_sort_dfs())
