"""Number of connected components in an undirected graph (DFS)."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def dfs(cur_node, adjacency_table, is_visited):
    """
    adjacency_table: list of lists. If there is an edge between node 0 and
        node 5, then adjacency_table[0] contains 5.
    is_visited: indicates if a node has already been visited
    """
    is_visited[cur_node] = True
    for cur_neighbor in adjacency_table[cur_node]:
        if not is_visited[cur_neighbor]:
            dfs(cur_neighbor, adjacency_table, is_visited)


def connected_components(adjacency_table, num_nodes):
    """Each DFS from an unvisited node discovers a new component."""
    is_visited = [False] * num_nodes
    count = 0
    for i in range(num_nodes):
        if not is_visited[i]:
            dfs(i, adjacency_table, is_visited)
            count += 1
    return count


def test_01():
    # One connected component: 0-1, 0-2, 0-3, 1-2, 1-3, 2-3
    adjacency_table = [[1, 2, 3], [2, 3], [3], []]
    if connected_components(adjacency_table, 4) != 1:
        handle_error()


def test_02():
    # 3 connected components: 0-1, 0-2, 0-3 / 4-5, 5-6 / 7-7
    adjacency_table = [[] for _ in range(8)]
    adjacency_table[0] = [1, 2, 3]
    adjacency_table[4] = [5]
    adjacency_table[5] = [6]
    adjacency_table[7] = [7]
    if connected_components(adjacency_table, 8) != 3:
        handle_error()


def test_03():
    # 8 nodes and no edges -> 8 components
    adjacency_table = [[] for _ in range(8)]
    if connected_components(adjacency_table, 8) != 8:
        handle_error()


def main():
    test_01()
    test_02()
    test_03()
    print("Test passed")


if __name__ == "__main__":
    main()
