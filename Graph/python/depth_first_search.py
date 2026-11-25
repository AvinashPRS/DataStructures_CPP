"""
Depth First Search Algorithm (https://en.wikipedia.org/wiki/Depth-first_search)

Author: Ayaan Khan (http://github.com/ayaankhan98)

Depth First Search also quoted as DFS is a Graph Traversal Algorithm.
Time Complexity O(|V| + |E|) where V is number of vertices and E is number of edges in graph.

Applications of Depth First Search are
1. Finding connected components
2. Finding 2-(edge or vertex)-connected components.
3. Finding 3-(edge or vertex)-connected components.
4. Finding the bridges of a graph.
5. Generating words in order to plot the limit set of a group.
6. Finding strongly connected components.

Working
1. Mark all vertices as unvisited first
2. start exploring from some starting vertex.
   While exploring vertex we mark the vertex as visited and start exploring the
   vertices connected to this vertex in recursive way.
"""


def add_edge(adj, u, v):
    """Adds an edge between u and v (1-indexed input) of an undirected graph."""
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)


def explore(adj, v, visited):
    """Explores the given vertex (traverses all vertices connected to it)."""
    print(v + 1, end=" ")
    visited[v] = True
    for x in adj[v]:
        if not visited[x]:
            explore(adj, x, visited)


def depth_first_search(adj, start):
    """Initiates depth first search algorithm from `start` (0-indexed)."""
    visited = [False] * len(adj)
    explore(adj, start, visited)


# Main function
if __name__ == "__main__":
    vertices = int(input("Enter the Vertices : "))
    edges = int(input("Enter the Edges : "))
    adj = [[] for _ in range(vertices)]  # creating graph
    print("Enter the vertices which have edges between them : ")
    for _ in range(edges):
        u, v = map(int, input().split())
        add_edge(adj, u, v)
    # running depth first search over graph
    depth_first_search(adj, 2)
    print()
