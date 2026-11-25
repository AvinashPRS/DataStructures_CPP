from collections import deque


# BFS Traversal of an undirected and unweighted graph.
def create_and_add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)  # do this because undirected graph


def bfs(adj_list, visited_vertex, source):
    visited_vertex = list(visited_vertex)  # passed by value in the C++ version
    q = deque([source])  # set up Queue for BFS
    out = []
    while q:
        v = q.popleft()
        visited_vertex[v] = True
        out.append(str(v))  # Print Vertex
        # visit all the children:
        for nb in adj_list[v]:
            if not visited_vertex[nb]:
                q.append(nb)  # Push unvisited vertex onto the queue
                visited_vertex[nb] = True
    print(" ".join(out))


# main code harness:
if __name__ == "__main__":
    num_vertices = 6  # 6 vertices (0,1,2,3,4,5)
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
    bfs(adj_list, visited_vertex, source)  # Should Print: 0 1 2 5 3 4
