import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def dfs(cur_node, adjacency_table, is_visited):
    """Helper function that performs depth first search on the graph.
    adjacency_table: list of lists. If there is an edge between node 0 and node 5,
                     then adjacency_table[0] stores 5 in it.
    is_visited: indicates if a node has already been visited or not
    """
    is_visited[cur_node] = True
    # Go through all the neighbors of the current node
    for cur_neighbor in adjacency_table[cur_node]:
        # If the current neighbor has not been visited, recursively call dfs on it
        if not is_visited[cur_neighbor]:
            dfs(cur_neighbor, adjacency_table, is_visited)


def connected_components(adjacency_table, num_nodes):
    """Compute number of connected components in an undirected graph."""
    is_visited = [False] * num_nodes
    # Each time we perform DFS on a node that has not been visited so far,
    # increment the number of connected components
    count = 0
    for i in range(num_nodes):
        if not is_visited[i]:
            dfs(i, adjacency_table, is_visited)
            count += 1
    return count


def test_01():
    # One connected component: edges 0-1, 0-2, 0-3, 1-2, 1-3 and 2-3
    adj = [[] for _ in range(4)]
    adj[0] += [1, 2, 3]
    adj[1] += [2, 3]
    adj[2] += [3]
    if connected_components(adj, 4) != 1:
        handle_error()


def test_02():
    # 3 connected components: 0-1, 0-2, 0-3 | 4-5, 5-6 | 7-7
    adj = [[] for _ in range(8)]
    adj[0] += [1, 2, 3]
    adj[4].append(5)
    adj[5].append(6)
    adj[7].append(7)
    if connected_components(adj, 8) != 3:
        handle_error()


def test_03():
    # 8 nodes and no edges -> 8 components
    adj = [[] for _ in range(8)]
    if connected_components(adj, 8) != 8:
        handle_error()


# main code harness:
if __name__ == "__main__":
    test_01()
    test_02()
    test_03()
    print("Test passed")
