"""BFS traversal of an undirected, unweighted graph."""
from collections import deque


def create_and_add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)  # undirected graph


def bfs(adj_list, visited_vertex, source):
    q = deque([source])
    visited_vertex = list(visited_vertex)  # passed by value in the C++ code
    out = []
    while q:
        v = q.popleft()
        visited_vertex[v] = True
        out.append(str(v))
        for child in adj_list[v]:
            if not visited_vertex[child]:
                q.append(child)
                visited_vertex[child] = True
    print(" ".join(out) + " ")


def main():
    num_vertices = 6  # vertices 0..5
    source = 0
    adj_list = [[] for _ in range(num_vertices)]
    visited_vertex = [False] * num_vertices
    create_and_add_edge(adj_list, 0, 1)
    create_and_add_edge(adj_list, 0, 2)
    create_and_add_edge(adj_list, 1, 5)
    create_and_add_edge(adj_list, 2, 3)
    create_and_add_edge(adj_list, 2, 4)
    create_and_add_edge(adj_list, 3, 3)
    create_and_add_edge(adj_list, 4, 4)
    create_and_add_edge(adj_list, 5, 5)
    bfs(adj_list, visited_vertex, source)  # Should print: 0 1 2 5 3 4


if __name__ == "__main__":
    main()
