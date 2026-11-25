import sys

WHITE, GRAY, BLACK = 0, 1, 2


def handle_error():
    print("Test failed")
    sys.exit(1)


def dfs(cur_node, adjacency_table, color):
    """Return True if a cycle is reachable from cur_node in the directed graph."""
    # Gray: we have started processing this node
    color[cur_node] = GRAY
    for cur_neighbor in adjacency_table[cur_node]:
        # If we find a neighboring node with the gray color, then we have found a loop
        if color[cur_neighbor] == GRAY:
            return True
        # If the neighboring node is white, perform DFS on it
        if color[cur_neighbor] == WHITE and dfs(cur_neighbor, adjacency_table, color):
            return True
    # Black: finished processing it
    color[cur_node] = BLACK
    return False


def is_cycle_present(adjacency_table, num_nodes):
    """True if cycle is present in directed graph, False otherwise."""
    color = [WHITE] * num_nodes
    for i in range(num_nodes):
        if color[i] == WHITE and dfs(i, adjacency_table, color):
            return True
    return False


def test_01():
    # No cycle: 0->1, 0->2, 0->3, 1->2, 1->3, 2->3, 4->1
    adj = [[1, 2, 3], [2, 3], [3], [], [1]]
    if is_cycle_present(adj, 5) is not False:
        handle_error()


def test_02():
    # Cycle 2->3, 3->4, 4->2
    adj = [[1, 2, 3], [2, 3], [3], [4], [2]]
    if is_cycle_present(adj, 5) is not True:
        handle_error()


# main code harness:
if __name__ == "__main__":
    test_01()
    test_02()
    print("Test passed")
