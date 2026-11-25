"""
Depth First Search (DFS) graph traversal. O(|V| + |E|).

Applications: connected components, 2/3-connected components, bridges,
strongly connected components, and more.

Working:
1. Mark all vertices as unvisited.
2. Start exploring from some starting vertex; mark it visited and recursively
   explore the vertices connected to it.
"""
import sys


def add_edge(adj, u, v):
    """Undirected graph: vertices are 1-indexed in input, 0-indexed in adj."""
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)


def explore(adj, v, visited, out):
    out.append(str(v + 1))
    visited[v] = True
    for x in adj[v]:
        if not visited[x]:
            explore(adj, x, visited, out)


def depth_first_search(adj, start):
    visited = [False] * len(adj)
    out = []
    explore(adj, start, visited, out)
    print(" ".join(out) + " ", end="")


def main():
    sys.setrecursionlimit(100000)
    tokens = iter(sys.stdin.read().split())
    print("Enter the Vertices : ", end="")
    vertices = int(next(tokens))
    print("Enter the Edges : ", end="")
    edges = int(next(tokens))

    adj = [[] for _ in range(vertices)]
    print("Enter the vertices which have edges between them : ")
    for _ in range(edges):
        u, v = int(next(tokens)), int(next(tokens))
        add_edge(adj, u, v)

    # running depth first search over graph (starting at index 2, i.e. vertex 3)
    depth_first_search(adj, 2)
    print()


if __name__ == "__main__":
    main()
