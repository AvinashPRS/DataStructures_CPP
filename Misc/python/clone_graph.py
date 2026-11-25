"""
Given a vertex of a directed graph, clone the graph reachable from that vertex.

Input: vertex (label + list of edges)
Output: list of cloned vertices; the first is the clone of the input vertex.

We traverse the graph (DFS or BFS), use a hash table keyed by label to track
visited vertices, and clone every edge as we go.
    TC: O(V + E)
    SC: O(V + E)
"""
from collections import deque


class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = []


def create_graph(count):
    return [Vertex(i) for i in range(count)]


def add_edge(u, v):
    u.edges.append(v)


def print_graph(g):
    for node in g:
        print(f"{node.data}: " + "".join(f"{e.data} " for e in node.edges))


def do_dfs(u_orig, u_copy, clone, visited):
    visited[u_orig.data] = u_copy
    for v in u_orig.edges:
        if v.data not in visited:
            v_copy = Vertex(v.data)
            clone.append(v_copy)
            do_dfs(v, v_copy, clone, visited)
        # create a copy of the edge
        u_copy.edges.append(visited[v.data])


def do_bfs(u_orig, u_copy, clone, visited):
    q = deque([u_orig])
    visited[u_orig.data] = u_copy
    while q:
        curr = q.popleft()
        for v in curr.edges:
            if v.data not in visited:
                v_copy = Vertex(v.data)
                clone.append(v_copy)
                q.append(v)
                visited[v.data] = v_copy
            # clone the edge
            visited[curr.data].edges.append(visited[v.data])


def clone_graph(u, method="DFS"):
    if not u:
        return []
    clone = []
    visited = {}  # label -> cloned vertex
    u_copy = Vertex(u.data)
    clone.append(u_copy)
    if method == "DFS":
        do_dfs(u, u_copy, clone, visited)
    elif method == "BFS":
        do_bfs(u, u_copy, clone, visited)
    return clone


def main():
    g = create_graph(5)
    add_edge(g[0], g[1])
    add_edge(g[1], g[2])
    add_edge(g[2], g[0])
    add_edge(g[2], g[3])
    add_edge(g[3], g[4])
    print_graph(g)

    print("\nDFS")
    print_graph(clone_graph(g[0], "DFS"))

    print("\nBFS")
    print_graph(clone_graph(g[0], "BFS"))


if __name__ == "__main__":
    main()
