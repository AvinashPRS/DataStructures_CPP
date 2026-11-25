"""
Graph toolkit: DFS, BFS, Union-Find, Topological sorting, Kruskal & Prim MST,
Bellman-Ford, Dijkstra and Floyd-Warshall on an adjacency-list graph of Vertex objects.

NOTE on differences from the C++ original:
- Distances use float('inf') instead of INT_MAX, so Bellman-Ford no longer overflows when
  relaxing an edge out of an unreached vertex.
- Prim's loop stops when the heap is empty (the C++ loop could pop from an empty heap).
"""
import heapq
import itertools
from collections import deque

INF = float("inf")


class WeightedEdge:
    """Weighted Edge of graph."""

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Vertex:
    """Graph node. To know if an edge exists TC: O(V + E)."""

    def __init__(self, data):
        self.data = data
        self.edges = []


def create_node(data):
    return Vertex(data)


def add_edge(g, src, dst, weight=1):
    """Adds a directed edge between two vertices."""
    g[src].edges.append(WeightedEdge(src, dst, weight))


def _dfs_helper(g, curr, visited):
    # if the current is visited return
    if curr in visited:
        return
    visited.add(curr)  # mark current as visited
    print(curr.data, end=" ")
    for e in curr.edges:  # traverse its edges
        _dfs_helper(g, g[e.end], visited)


def DFS(g):
    """Driver for DFS of graph. TC: O(V + E)"""
    visited = set()
    # start traversal from each vertex to cover the disconnected graph case as well
    for v in g:
        _dfs_helper(g, v, visited)


def BFS(g):
    """BFS of graph. TC: O(V + E).
    (Like the C++ version, vertices are marked visited when popped, not when pushed.)"""
    visited = set()
    for v in g:
        q = deque()
        # add the starting node only if it is not visited yet
        if v not in visited:
            q.append(v)
        while q:
            curr = q.popleft()
            visited.add(curr)  # mark as visited
            print(curr.data, end=" ")
            for e in curr.edges:  # add its next edge nodes
                if g[e.end] not in visited:
                    q.append(g[e.end])


def print_graph(g):
    for v in g:
        print(f"{v.data}: " + "".join(f"{g[e.end].data} " for e in v.edges))


def print_mst(mst):
    """Prints the Minimum Spanning Tree."""
    for i, edges in enumerate(mst):
        print(f"{i}: " + "".join(f"{e.end}({e.weight}), " for e in edges))


def create_graph(n_vertices):
    return [create_node(i) for i in range(n_vertices)]


# ----------------------------------------- UNION-FIND -----------------------------------------
class UnionFind:
    """Union-Find with weighted Union and path compression. TC: O(logN) for each union-find."""

    def __init__(self, n_nodes):
        # for keeping track of root and size of components
        self.root = list(range(n_nodes))
        self.size = [1] * n_nodes

    def get_root(self, idx):
        """Finds the root of component (with path halving)."""
        while self.root[idx] != idx:
            self.root[idx] = self.root[self.root[idx]]
            idx = self.root[idx]
        return idx

    def union(self, a, b):
        """Union operation using Weight consideration. TC: O(log2N)
        Based on the sizes of both components, the root of the smaller component becomes part
        of the bigger one. This keeps trees shallow."""
        ra, rb = self.get_root(a), self.get_root(b)
        if ra == rb:
            return
        if self.size[rb] < self.size[ra]:
            self.root[rb] = ra
            self.size[ra] += self.size[rb]
        else:
            self.root[ra] = rb
            self.size[rb] += self.size[ra]

    def find(self, a, b):
        """Find operation using Path Compression. TC: O(log2N), N: no. of nodes"""
        return self.get_root(a) == self.get_root(b)

    def connected_components(self):
        """Prints the number of elements in each component."""
        result = sorted(self.size[i] for i in range(len(self.root)) if self.root[i] == i)
        print(" ".join(map(str, result)), end=" ")
        return result


# ------------------------------------ TOPOLOGICAL SORTING ------------------------------------
"""
TOPOLOGICAL SORTING
TC: O(V + E)
SC: O(V + E)

Gives ordering of vertices such that all the source vertices come before the destination
vertices for edges.

The idea is to do a modified DFS. Instead of processing the current vertex, go recurse for its
adjacent unvisited neighbours first. This way the parent node will be emitted at the end.

To detect a cycle we keep track of vertices in the recursion stack of the current branch.
"""


def _topological_sort_dfs(src, g, order, visited):
    """Modified version of DFS (post-order)."""
    visited[src] = True
    for e in g[src].edges:
        if not visited[e.end]:
            _topological_sort_dfs(e.end, g, order, visited)
    order.append(src)  # add to order


def all_topological_sort_orders(g):
    """Topological (post-)order starting from each vertex."""
    n = len(g)
    all_orders = []
    for i in range(n):
        order = deque()
        visited = [False] * n
        visited[i] = True
        _topological_sort_dfs(i, g, order, visited)
        all_orders.append(order)
    return all_orders


def _topological_dfs(curr, g, order, rec_stack, visited):
    """DFS Helper. Returns True in case of cycle else False."""
    # visited means the ordering from this node has already been added
    if visited[curr]:
        return False
    visited[curr] = True
    rec_stack[curr] = True  # add to recursion stack
    for e in g[curr].edges:
        # if the neighbour is in the recursion stack, there is a cycle
        if rec_stack[e.end]:
            return True
        elif _topological_dfs(e.end, g, order, rec_stack, visited):
            return True
    rec_stack[curr] = False  # remove current node of branch from the stack
    order.append(curr)       # add after processing its neighbours
    return False


def topological_dfs(g):
    """Using DFS. TC: O(V + E). Returns the post-order (reverse it for the topological order),
    or [] if there is a cycle."""
    n = len(g)
    visited, rec_stack, order = [False] * n, [False] * n, []
    for i in range(n):  # in case of disconnected graph
        if not visited[i] and _topological_dfs(i, g, order, rec_stack, visited):
            return []  # if there is a cycle return empty order
    return order


def topological_bfs(g):
    """Using BFS (Kahn). TC: O(V + E). Returns the order reversed (to match topological_dfs),
    or [] if there is a cycle."""
    order = []
    visited_vertices = 0
    # find the indegree of vertices
    indegree = [0] * len(g)
    for v in g:
        for e in v.edges:
            indegree[e.end] += 1
    q = deque(i for i in range(len(g)) if indegree[i] == 0)  # add the 0 indegree vertices
    while q:
        curr = q.popleft()
        order.append(curr)
        visited_vertices += 1
        # decrement the indegree of its neighbours
        for e in g[curr].edges:
            indegree[e.end] -= 1
            if indegree[e.end] == 0:
                q.append(e.end)
    order.reverse()  # return the order in reverse
    return [] if visited_vertices < len(g) else order


# ----------------------------------------------------------------------------------------------
#            BOTH PRIM AND KRUSKAL'S ALGO WORK ONLY FOR UNDIRECTED CONNECTED GRAPHS
# ------------------------------- KRUSKAL'S MINIMUM SPANNING TREE ------------------------------
"""
till edges are there:
    1. pick the smallest weight edge
    2. check if adding it would cause a cycle with the existing edges in the MST
    3. repeat step 2
"""


def kruskal_mst(n_vertices, edges):
    """TC: O(ElogE (sorting) + ElogV (Union-Find for all vertices))"""
    mst = [[] for _ in range(n_vertices)]
    edges.sort(key=lambda e: e.weight)  # sort the edges
    uf = UnionFind(n_vertices)
    cost = 0
    # Pick edges one by one, making sure that:
    # 1. The new edge doesn't create a cycle in the MST (endpoints not already connected)
    # 2. The edge picked is the smallest in weight possible at the moment
    for e in edges:
        if not uf.find(e.start, e.end):
            cost += e.weight
            mst[e.start].append(e)
            uf.union(e.start, e.end)  # vertices are connected now, Union them
    print(f"Kruskal MST cost:{cost}")
    return mst


# ------------------------------- PRIM'S MINIMUM SPANNING TREE -------------------------------
"""
Two sets are maintained, one which has all the vertices and the other empty initially.

With each vertex we associate the cut cost.
Cut cost of vertex u: cost of an edge involving vertex u.
Make the starting node's cut cost = 0.
while all the nodes are unvisited:
    pick the vertex with least cut cost, if it is unvisited
    add to mst set
    mark it visited
In order to prevent cycles we check if nodes are visited.
TC: O(E log E)
"""


def prim_mst(g):
    cost = 0
    n = len(g)
    processed_vertices = 1  # the start vertex
    mst = [[] for _ in range(n)]
    visited = [False] * n
    counter = itertools.count()
    min_heap = []  # min-heap for selecting the smallest edge weight vertex

    # we start with the first node and add all its neighbours
    visited[0] = True
    for e in g[0].edges:
        heapq.heappush(min_heap, (e.weight, next(counter), e))

    # We add only the edge with min weight that connects a vertex.
    # NOTE: multiple heap entries may lead to the same vertex, so check visited when popping.
    while min_heap and processed_vertices < n:
        _, _, curr = heapq.heappop(min_heap)
        if not visited[curr.end]:
            visited[curr.end] = True
            processed_vertices += 1
            mst[curr.start].append(curr)
            cost += curr.weight
            for e in g[curr.end].edges:  # add its non visited neighbours
                if not visited[e.end]:
                    heapq.heappush(min_heap, (e.weight, next(counter), e))
    print(f"Prim's cost:{cost}")
    return mst


# ---------------------------------- SHORTEST PATH ALGORITHMS ----------------------------------
def print_distances(distance):
    for i, d in enumerate(distance):
        print(f"[{i}]: {d}")


def print_all_distances(distance):
    """Prints distance between all the vertex pairs."""
    for i, row in enumerate(distance):
        print(f"[{i}]: " + "".join(("INF" if a == INF else str(a)) + " " for a in row))


def bellman_ford(g, src):
    """
    Used for finding the shortest path from a SOURCE vertex to all other vertices.
    USE: Used for finding the existence of negative cycles.

    The idea is to relax all the edges. A shortest path has at most V-1 edges (otherwise
    there would be a cycle).

    dist[V] = INF, dist[SRC] = 0
    for [1:V-1]:
        for each edge a->b:
            if W + dist[a] < dist[b]: update dist[b]
    then once more over every edge: if it still relaxes, report a negative cycle.

    TC: O(EV)
    """
    n = len(g)
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for v in g:  # traverse through all the edges, TC: O(V + E)
            for e in v.edges:
                if e.weight + dist[e.start] < dist[e.end]:
                    dist[e.end] = e.weight + dist[e.start]
    # check for negative cycle
    for v in g:
        for e in v.edges:
            if e.weight + dist[e.start] < dist[e.end]:
                print(f"Negative cycle in {e.start}---{e.weight}---->{e.end}")
    return dist


def djikstra(g, src, target):
    """
    Shortest distance between source vertex SRC and the target vertex.
    NOTE: Doesn't work with negative weights.
    TC: O(E + (V + E) * logV) ~ O(E log V)

    Why O(E + ElogV) and not O(E + ElogE)?
    In the worst case E = V^2, so O(logE) = O(log(V^2)) = 2 O(logV) = O(logV).

    1. set the distance for all the vertices as INF
    2. dist[src] = 0
    3. add the neighbouring vertices with their distance from source
    while min heap is not empty:
        take the current vertex and update its neighbours' dist if current is unvisited
    """
    n = len(g)
    visited = [False] * n
    distance = [INF] * n
    distance[src] = 0
    min_heap = [(0, src)]  # (distance, label)

    while min_heap:
        _, label = heapq.heappop(min_heap)
        if not visited[label]:
            visited[label] = True
            # if current is the target return (or continue for all vertices)
            if label == target:
                break
            for e in g[label].edges:
                # update the path distance iff the neighbour is unvisited and it improves
                if not visited[e.end] and e.weight + distance[label] < distance[e.end]:
                    distance[e.end] = e.weight + distance[label]
                    heapq.heappush(min_heap, (distance[e.end], e.end))
    return distance


def floyd_warshall(g):
    """
    All pair shortest distance. TC: O(V^3)
    DP: dist(i, j) = min(dist(i, j), dist(i, k) + dist(k, j)) for every intermediate k.
    """
    n = len(g)
    distance = [[INF] * n for _ in range(n)]
    # initial distance between vertices using the edge weights
    for v in g:
        for e in v.edges:
            distance[e.start][e.end] = e.weight
    for i in range(n):  # distance between the same vertex is zero
        distance[i][i] = 0

    print_all_distances(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    print()
    return distance


# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    g = create_graph(5)
    #   0-->1-->2-->3-->4
    #   ^       |
    #   |_______|
    add_edge(g, 0, 1)
    add_edge(g, 1, 2)
    add_edge(g, 2, 0)
    add_edge(g, 2, 3)
    add_edge(g, 3, 4)
    print_graph(g)

    print("DFS")
    DFS(g)
    print("\nBFS")
    BFS(g)
    print()

    # Kruskal's MST
    #   {0}----------7--------
    #   |                    |
    #   6                    |
    #   |                    |
    #   --->{3}---9---->{1}<--
    #       |             |
    #       8             6
    #       |             |
    #       -------->{2}<--
    n_vertices = 4
    g1 = create_graph(n_vertices)
    add_edge(g1, 0, 1, 7)
    add_edge(g1, 0, 3, 6)
    add_edge(g1, 3, 1, 9)
    add_edge(g1, 3, 2, 8)
    add_edge(g1, 1, 2, 6)
    edges = [WeightedEdge(*t) for t in [(0, 1, 7), (0, 3, 6), (3, 1, 9), (3, 2, 8), (1, 2, 6)]]
    print_mst(kruskal_mst(n_vertices, edges))
    print()
    # Prim's MST
    print_mst(prim_mst(g1))

    # Bellman Ford shortest path
    #   0 -4-> 1 -7-> 3,   0 -3-> 2 -(-2)-> 3
    g2 = create_graph(4)
    add_edge(g2, 0, 1, 4)
    add_edge(g2, 0, 2, 3)
    add_edge(g2, 1, 3, 7)
    add_edge(g2, 2, 3, -2)
    print("Bellman Ford:")
    print_distances(bellman_ford(g2, 0))

    # Djikstra shortest path
    #   0 -4-> 1 -7-> 3,   0 -3-> 2 -2-> 3
    src, target = 0, 3
    g3 = create_graph(4)
    add_edge(g3, 0, 1, 4)
    add_edge(g3, 0, 2, 3)
    add_edge(g3, 1, 3, 7)
    add_edge(g3, 2, 3, 2)
    print(f"\nDjikstra: \nSource: {src}, Target: {target}")
    print_distances(djikstra(g3, 0, 3))

    print("\nFloyd Warshall:")
    print_all_distances(floyd_warshall(g3))

    # Topological sort: all the topological sort orders
    print("\nTopological Sorting Orders:")
    for order in all_topological_sort_orders(g3):
        print(" ".join(str(x) for x in reversed(order)) + " ")

    print("\nBFS Topological Sorting:")
    print(" ".join(str(x) for x in reversed(topological_bfs(g3))) + " ")

    print("\nDFS Topological Sorting:")
    print(" ".join(str(x) for x in reversed(topological_dfs(g3))) + " ")
