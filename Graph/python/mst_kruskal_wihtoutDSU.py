"""
Given an undirected, connected and weighted graph, find Minimum Spanning Tree (MST)
of the graph using Kruskal's algorithm (cycle check via DFS instead of DSU).
"""
from dataclasses import dataclass


@dataclass
class Edge:
    src: int
    dest: int
    weight: int


# A standard DFS helper function to see if 'dest' is reachable from 'src'
def has_path(src, dest, parent, mst_adj):
    if src == dest:
        return True
    for neighbor in mst_adj[src]:
        if neighbor != parent:  # Avoid going back directly to the caller
            if has_path(neighbor, dest, src, mst_adj):
                return True
    return False


# Kruskal without DSU (Disjoint Set Union):
def kruskal_without_dsu(num_vertices, edges):
    # 1. Sort all edges in non-decreasing order of their weight
    edges.sort(key=lambda e: e.weight)

    # This adjacency list tracks the structural connections inside our growing MST
    mst_adj = [[] for _ in range(num_vertices)]
    mst_result = []
    total = 0

    # 2. Iterate through the sorted edges
    for e in edges:
        # If a path already exists between src and dest in our current MST,
        # adding this edge forms a cycle.
        if not has_path(e.src, e.dest, -1, mst_adj):
            mst_adj[e.src].append(e.dest)
            mst_adj[e.dest].append(e.src)
            mst_result.append(e)
            total += e.weight
        # Optimization: Stop early if we have collected V - 1 edges
        if len(mst_result) == num_vertices - 1:
            break

    print("Edges in the constructed MST:")
    for e in mst_result:
        print(f"{e.src} -- {e.dest} == {e.weight}")
    print("Minimum Spanning Tree Total Weight:", total)


# main code harness:
if __name__ == "__main__":
    edges = [Edge(0, 1, 10), Edge(0, 2, 6), Edge(0, 3, 5), Edge(1, 3, 15), Edge(2, 3, 4)]
    kruskal_without_dsu(4, edges)
