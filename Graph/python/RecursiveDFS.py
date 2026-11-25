# Author: Aakash Prabhu


# Recursive DFS Traversal of an undirected and unweighted graph.
def create_and_add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)  # do this because undirected graph


def recursive_dfs(adj_list, visited_vertex, source):
    # NOTE: the C++ version passes visitedVertex by value; that only works there because
    # each recursive call copies it. Here we share one list, which is the correct DFS.
    visited_vertex[source] = True
    print(source, end=" ")  # Print Vertex
    for nb in adj_list[source]:
        if not visited_vertex[nb]:
            recursive_dfs(adj_list, visited_vertex, nb)  # Go as far as possible by recursing.


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
    create_and_add_edge(adj_list, 3, 3)  # Do this because no children!
    create_and_add_edge(adj_list, 4, 4)
    create_and_add_edge(adj_list, 2, 2)
    recursive_dfs(adj_list, visited_vertex, source)
    print()
    # Should Print: 0 1 3 4 2
