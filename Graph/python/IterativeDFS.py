# Author: Aakash Prabhu


# DFS Traversal of an undirected and unweighted graph.
def create_and_add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)  # do this because undirected graph


def dfs(adj_list, visited_vertex, source):
    visited_vertex = list(visited_vertex)
    s = [source]  # stack
    out = []
    while s:
        v = s.pop()
        visited_vertex[v] = True
        out.append(str(v))  # Print Vertex
        for nb in adj_list[v]:  # Go as far as we can go and then backtrack
            if not visited_vertex[nb]:
                s.append(nb)  # Push unvisited vertex onto the stack
                visited_vertex[nb] = True
    print(" ".join(out))


# main code harness:
if __name__ == "__main__":
    num_vertices = 5
    source = 0
    adj_list = [[] for _ in range(num_vertices)]
    visited_vertex = [False] * num_vertices
    create_and_add_edge(adj_list, 0, 1)
    create_and_add_edge(adj_list, 0, 2)
    create_and_add_edge(adj_list, 1, 3)
    create_and_add_edge(adj_list, 1, 4)
    create_and_add_edge(adj_list, 3, 3)
    create_and_add_edge(adj_list, 4, 4)
    create_and_add_edge(adj_list, 2, 2)
    dfs(adj_list, visited_vertex, source)  # Should Print: 0 2 1 4 3
