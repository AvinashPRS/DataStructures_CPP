"""
Graph algorithms collection:
DFS, BFS, Union-Find, topological sort (DFS & BFS), Kruskal & Prim MST,
Bellman-Ford, Dijkstra and Floyd-Warshall.

Run with --dfs-vs-topo to see the (commented-out in C++) demo contrasting a
plain DFS order with a topological order.
"""
import heapq
import itertools
import sys
from collections import deque

INT_MAX = 2**31 - 1


class WeightedEdge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Vertex:
    """Graph node. Checking whether an edge exists is O(V + E)."""

    def __init__(self, data):
        self.data = data
        self.edges = []


def create_graph(n_vertices):
    return [Vertex(i) for i in range(n_vertices)]


def add_edge(g, src, dst, weight=1):
    g[src].edges.append(WeightedEdge(src, dst, weight))


def _dfs_helper(g, curr, visited, out):
    if curr in visited:
        return
    visited.add(curr)
    out.append(f"{curr.data} ")
    for edge in curr.edges:
        _dfs_helper(g, g[edge.end], visited, out)


def dfs(g):
    """DFS from every vertex to also cover disconnected graphs. O(V + E)"""
    visited = set()
    out = []
    for v in g:
        _dfs_helper(g, v, visited, out)
    print("".join(out), end="")


def bfs(g):
    """BFS of graph. O(V + E)"""
    visited = set()
    out = []
    for v in g:
        q = deque()
        if v not in visited:
            q.append(v)
        while q:
            curr = q.popleft()
            visited.add(curr)
            out.append(f"{curr.data} ")
            for edge in curr.edges:
                if g[edge.end] not in visited:
                    q.append(g[edge.end])
    print("".join(out), end="")


def print_graph(g):
    for v in g:
        print(f"{v.data}: " + "".join(f"{g[e.end].data} " for e in v.edges))


def print_mst(mst):
    for i, edges in enumerate(mst):
        print(f"{i}: " + "".join(f"{e.end}({e.weight}), " for e in edges))


# ---------------------------------------------------------------------------
# UNION-FIND with weighted union and path compression. O(log N) per op.
# ---------------------------------------------------------------------------
class UnionFind:
    def __init__(self, n_nodes):
        self.root_ = list(range(n_nodes))
        self.size_ = [1] * n_nodes

    def get_root(self, idx):
        while self.root_[idx] != idx:
            self.root_[idx] = self.root_[self.root_[idx]]  # path halving
            idx = self.root_[idx]
        return idx

    def union(self, a, b):
        """Attach the smaller component under the root of the larger one."""
        root_a = self.get_root(a)
        root_b = self.get_root(b)
        if self.size_[root_b] < self.size_[root_a]:
            self.root_[root_b] = root_a
            self.size_[root_a] += self.size_[root_b]
        else:
            self.root_[root_a] = self.root_[root_b]
            self.size_[root_b] += self.size_[root_a]

    def find(self, a, b):
        return self.get_root(a) == self.get_root(b)

    def connected_components(self):
        """Prints the sizes of the components in ascending order."""
        result = sorted(self.size_[i] for i in range(len(self.root_))
                        if self.root_[i] == i)
        print("".join(f"{a} " for a in result), end="")


# ---------------------------------------------------------------------------
# TOPOLOGICAL SORTING. O(V + E) time and space.
# Orders vertices so that sources of edges come before destinations.
# Modified DFS: recurse into unvisited neighbours first, then record the
# current vertex. To detect cycles, track vertices in the recursion stack.
# ---------------------------------------------------------------------------
def topological_sort_dfs(src, g, order, visited):
    visited[src] = True
    for edge in g[src].edges:
        if not visited[edge.end]:
            topological_sort_dfs(edge.end, g, order, visited)
    order.append(src)


def all_topological_sort_orders(g):
    """Topological sort starting from each vertex."""
    n_vertices = len(g)
    all_orders = []
    for i in range(n_vertices):
        order = []
        visited = [False] * n_vertices
        visited[i] = True
        topological_sort_dfs(i, g, order, visited)
        all_orders.append(order)
    return all_orders


def _topological_dfs_helper(curr, g, order, rec_stack, visited):
    """Returns True in case of a cycle."""
    if visited[curr]:
        return False
    visited[curr] = True
    rec_stack[curr] = True
    for edge in g[curr].edges:
        if rec_stack[edge.end]:
            return True
        if _topological_dfs_helper(edge.end, g, order, rec_stack, visited):
            return True
    rec_stack[curr] = False
    order.append(curr)
    return False


def topological_dfs(g):
    """Returns the (reversed) topological order, or [] if there is a cycle."""
    n = len(g)
    visited = [False] * n
    rec_stack = [False] * n
    order = []
    for i in range(n):
        if not visited[i]:
            if _topological_dfs_helper(i, g, order, rec_stack, visited):
                return []
    return order


def topological_bfs(g):
    """Kahn's algorithm. Returns the order reversed, or [] if there is a cycle."""
    order = []
    visited_vertices = 0
    indegree = [0] * len(g)
    for v in g:
        for edge in v.edges:
            indegree[edge.end] += 1
    q = deque(i for i, d in enumerate(indegree) if d == 0)
    while q:
        curr = q.popleft()
        order.append(curr)
        visited_vertices += 1
        for edge in g[curr].edges:
            indegree[edge.end] -= 1
            if indegree[edge.end] == 0:
                q.append(edge.end)
    order.reverse()
    return [] if visited_vertices < len(g) else order


# ---------------------------------------------------------------------------
# BOTH PRIM AND KRUSKAL WORK ONLY FOR UNDIRECTED CONNECTED GRAPHS
# ---------------------------------------------------------------------------
def kruskal_mst(n_vertices, edges):
    """
    Repeatedly pick the smallest edge that doesn't create a cycle.
    O(E log E (sorting) + E log V (union-find))
    """
    mst = [[] for _ in range(n_vertices)]
    edges.sort(key=lambda e: e.weight)
    uf = UnionFind(n_vertices)
    cost = 0
    for edge in edges:
        src, dst = edge.start, edge.end
        # if the endpoints are already connected the edge would form a cycle
        if not uf.find(src, dst):
            cost += edge.weight
            mst[src].append(edge)
            uf.union(src, dst)
    print(f"Kruskal MST cost:{cost}")
    return mst


def prim_mst(g):
    """
    Grow the MST from vertex 0, always adding the cheapest edge that leads to
    an unvisited vertex. O(E log E)

    Note: the C++ loop runs `while processed < n_vertices` without counting the
    start vertex, which pops from an empty heap; here we also stop when the
    heap is empty.
    """
    cost = 0
    n_vertices = len(g)
    processed_vertices = 0
    mst = [[] for _ in range(n_vertices)]
    visited = [False] * n_vertices
    counter = itertools.count()  # tie-breaker for equal weights
    min_heap = []

    visited[0] = True
    for edge in g[0].edges:
        heapq.heappush(min_heap, (edge.weight, next(counter), edge))

    while processed_vertices < n_vertices and min_heap:
        _, _, curr = heapq.heappop(min_heap)
        if not visited[curr.end]:
            visited[curr.end] = True
            processed_vertices += 1
            mst[curr.start].append(curr)
            cost += curr.weight
            for edge in g[curr.end].edges:
                if not visited[edge.end]:
                    heapq.heappush(min_heap, (edge.weight, next(counter), edge))

    print(f"Prim's cost:{cost}")
    return mst


# ---------------------------------------------------------------------------
# SHORTEST PATH ALGORITHMS
# ---------------------------------------------------------------------------
def print_distances(distance):
    for i, d in enumerate(distance):
        print(f"[{i}]: {d}")


def print_all_distances(distance):
    for i, row in enumerate(distance):
        print(f"[{i}]: " + "".join(("INF" if a == INT_MAX else str(a)) + " "
                                    for a in row))


def bellman_ford(g, src):
    """
    Shortest paths from SRC; also detects negative cycles.
    Relax every edge V-1 times, then one more pass reports negative cycles.
    O(EV)
    """
    n = len(g)
    dist = [INT_MAX] * n
    dist[src] = 0
    for _ in range(n - 1):
        for v in g:
            for edge in v.edges:
                if dist[edge.start] != INT_MAX and \
                        edge.weight + dist[edge.start] < dist[edge.end]:
                    dist[edge.end] = edge.weight + dist[edge.start]
    for v in g:
        for edge in v.edges:
            if dist[edge.start] != INT_MAX and \
                    edge.weight + dist[edge.start] < dist[edge.end]:
                print(f"Negative cycle in {edge.start}---{edge.weight}---->{edge.end}")
    return dist


def djikstra(g, src, target):
    """
    Shortest distance from SRC (stops once TARGET is finalised).
    Doesn't work with negative weights. O(E log V)
    """
    n = len(g)
    visited = [False] * n
    distance = [INT_MAX] * n
    distance[src] = 0
    min_heap = [(0, src)]
    while min_heap:
        _, label = heapq.heappop(min_heap)
        if not visited[label]:
            visited[label] = True
            if label == target:
                break
            for edge in g[label].edges:
                if not visited[edge.end] and \
                        edge.weight + distance[label] < distance[edge.end]:
                    distance[edge.end] = edge.weight + distance[label]
                    heapq.heappush(min_heap, (distance[edge.end], edge.end))
    return distance


def floyd_warshall(g):
    """
    All-pairs shortest distance. O(V^3)
    dist(i, j) = min(dist(i, j), dist(i, k) + dist(k, j))
    """
    n = len(g)
    distance = [[INT_MAX] * n for _ in range(n)]
    for v in g:
        for edge in v.edges:
            distance[edge.start][edge.end] = edge.weight
    for i in range(n):
        distance[i][i] = 0

    print_all_distances(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] == INT_MAX or distance[k][j] == INT_MAX:
                    continue
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    print()
    return distance


# ---------------------------------------------------------------------------
# Demo: difference between plain DFS (pre-order) and topological sort
# (post-order, reversed).
# ---------------------------------------------------------------------------
def demo_dfs_vs_topo():
    num_vertices = 6
    adj = [[] for _ in range(num_vertices)]
    for u, v in [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]:
        adj[u].append(v)

    def standard_dfs(u, visited, out):
        visited[u] = True
        out.append(u)  # record as soon as we visit it
        for v in adj[u]:
            if not visited[v]:
                standard_dfs(v, visited, out)

    def topo_helper(u, visited, stack):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                topo_helper(v, visited, stack)
        stack.append(u)  # after all dependencies are explored

    visited, dfs_result = [False] * num_vertices, []
    for i in range(num_vertices):
        if not visited[i]:
            standard_dfs(i, visited, dfs_result)
    print("Standard DFS Traversal Order: " + "".join(f"{n} " for n in dfs_result))

    visited, topo_stack = [False] * num_vertices, []
    for i in range(num_vertices):
        if not visited[i]:
            topo_helper(i, visited, topo_stack)
    print("Topological Sort Order:       " +
          "".join(f"{n} " for n in reversed(topo_stack)))


def main():
    if "--dfs-vs-topo" in sys.argv:
        demo_dfs_vs_topo()
        return

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
    dfs(g)
    print("\nBFS")
    bfs(g)
    print()

    # Kruskal's MST
    n_vertices = 4
    g1 = create_graph(n_vertices)
    add_edge(g1, 0, 1, 7)
    add_edge(g1, 0, 3, 6)
    add_edge(g1, 3, 1, 9)
    add_edge(g1, 3, 2, 8)
    add_edge(g1, 1, 2, 6)
    edges = [WeightedEdge(0, 1, 7), WeightedEdge(0, 3, 6), WeightedEdge(3, 1, 9),
             WeightedEdge(3, 2, 8), WeightedEdge(1, 2, 6)]
    print_mst(kruskal_mst(n_vertices, edges))
    print()
    # Prim's MST
    print_mst(prim_mst(g1))

    # Bellman Ford shortest path (with a negative edge)
    g2 = create_graph(4)
    add_edge(g2, 0, 1, 4)
    add_edge(g2, 0, 2, 3)
    add_edge(g2, 1, 3, 7)
    add_edge(g2, 2, 3, -2)
    print("Bellman Ford:")
    print_distances(bellman_ford(g2, 0))

    # Dijkstra shortest path
    src, target = 0, 3
    g3 = create_graph(4)
    add_edge(g3, 0, 1, 4)
    add_edge(g3, 0, 2, 3)
    add_edge(g3, 1, 3, 7)
    add_edge(g3, 2, 3, 2)
    print(f"\nDjikstra: \nSource: {src}, Target: {target}")
    print_distances(djikstra(g3, src, target))

    print("\nFloyd Warshall:")
    print_all_distances(floyd_warshall(g3))

    # Topological sort orders from every start vertex
    print("\nTopological Sorting Orders:")
    for order in all_topological_sort_orders(g3):
        print("".join(f"{v} " for v in reversed(order)))

    print("\nBFS Topological Sorting:")
    print("".join(f"{v} " for v in reversed(topological_bfs(g3))))

    print("\nDFS Topological Sorting:")
    print("".join(f"{v} " for v in reversed(topological_dfs(g3))))


if __name__ == "__main__":
    main()
