"""
Minimum Spanning Tree (MST)

Find a subset of edges in a connected, edge-weighted, undirected graph G = (V, E) that connects
all vertices without any cycles, while minimising the total edge weight. A spanning tree uses
exactly |V| - 1 edges.

Recommended Implementation Choice
- Kruskal's Algorithm for sparse graphs: sorts all edges globally and uses Union-Find to avoid cycles.
- Prim's Algorithm for dense graphs: grows outward from a start node using a priority queue.

How MST Algorithms Handle Cycles
- Kruskal: if two endpoints already share the same root in Union-Find, adding that edge would
  complete a cycle, so it is skipped.
- Prim: only considers edges that connect a visited vertex to an unvisited vertex, which naturally
  ignores any edge that loops back to an already-visited node.
"""
import heapq
import itertools


class WeightedEdge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = []


class UnionFind:
    """Disjoint Set Union: tracks which nodes belong to the same connected group, letting
    Kruskal's algorithm quickly detect if adding an edge would create a cycle."""

    def __init__(self, n_nodes):
        self.root = list(range(n_nodes))
        self.size = [1] * n_nodes

    def get_root(self, idx):
        if idx == self.root[idx]:
            return idx
        self.root[idx] = self.get_root(self.root[idx])  # Path compression
        return self.root[idx]

    def union(self, a, b):
        ra, rb = self.get_root(a), self.get_root(b)
        if ra == rb:
            return
        # union by size
        if self.size[rb] < self.size[ra]:
            self.root[rb] = ra
            self.size[ra] += self.size[rb]
        else:
            self.root[ra] = rb
            self.size[rb] += self.size[ra]


# --- 1. Kruskal's Algorithm ---  Time O(E log E), Space O(V + E)
def kruskal_mst(g):
    n = len(g)
    # 1. Gather all unique edges (avoid processing both src->dest and dest->src)
    all_edges = [e for v in g for e in v.edges if e.start < e.end]
    # 2. Sort all edges in non-decreasing order of their weights (stable, like the C++ result)
    all_edges.sort(key=lambda e: e.weight)
    uf = UnionFind(n)
    mst = []
    # 3. Pick the smallest non-cycling edges
    for e in all_edges:
        if uf.get_root(e.start) != uf.get_root(e.end):
            uf.union(e.start, e.end)
            mst.append(e)
        if len(mst) == n - 1:  # An MST always has exactly V - 1 edges
            break
    return mst


# --- 2. Prim's Algorithm ---  Time O(E log V), Space O(V + E)
def prim_mst(g, start_node=0):
    n = len(g)
    mst = []
    in_mst = [False] * n
    counter = itertools.count()  # tie-breaker so heapq never compares edge objects
    pq = []

    in_mst[start_node] = True
    for e in g[start_node].edges:
        heapq.heappush(pq, (e.weight, next(counter), e))

    while pq and len(mst) < n - 1:
        _, _, e = heapq.heappop(pq)
        nxt = e.end
        # If the destination is already in the MST, skip it to prevent cycles
        if in_mst[nxt]:
            continue
        in_mst[nxt] = True
        mst.append(e)
        # Feed all unvisited outward edges from this new vertex into the queue
        for out in g[nxt].edges:
            if not in_mst[out.end]:
                heapq.heappush(pq, (out.weight, next(counter), out))
    return mst


def print_mst_result(algo_name, mst):
    print(f"--- {algo_name} MST Output ---")
    total = 0
    for e in mst:
        print(f"{e.start} - {e.end} (Weight: {e.weight})")
        total += e.weight
    print(f"Total MST Weight Cost: {total}\n")


# main code harness:
if __name__ == "__main__":
    graph = [Vertex(i) for i in range(6)]

    # Edge additions must be bidirectional for proper MST evaluation
    def add_undirected_edge(src, dst, w):
        graph[src].edges.append(WeightedEdge(src, dst, w))
        graph[dst].edges.append(WeightedEdge(dst, src, w))

    for s, d, w in [(0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 3, 3), (2, 3, 1),
                    (2, 4, 4), (3, 4, 2), (3, 5, 4), (4, 5, 3)]:
        add_undirected_edge(s, d, w)

    print_mst_result("Kruskal's Algorithm", kruskal_mst(graph))
    print_mst_result("Prim's Algorithm", prim_mst(graph, 0))
