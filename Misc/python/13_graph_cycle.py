"""Detect a cycle in a directed graph using DFS with white/gray/black colors."""
import sys

WHITE = 0  # not yet processed
GRAY = 1   # processing started
BLACK = 2  # processing finished


def handle_error():
    print("Test failed")
    sys.exit(1)


def dfs(cur_node, adjacency_table, color):
    """Returns True if a cycle is reachable from cur_node."""
    color[cur_node] = GRAY
    for cur_neighbor in adjacency_table[cur_node]:
        # A gray neighbour means we found a loop
        if color[cur_neighbor] == GRAY:
            return True
        if color[cur_neighbor] == WHITE:
            if dfs(cur_neighbor, adjacency_table, color):
                return True
    color[cur_node] = BLACK
    return False


def is_cycle_present(adjacency_table, num_nodes):
    color = [WHITE] * num_nodes
    for i in range(num_nodes):
        if color[i] == WHITE:
            if dfs(i, adjacency_table, color):
                return True
    return False


def test_01():
    # No cycle: 0->1, 0->2, 0->3, 1->2, 1->3, 2->3, 4->1
    adjacency_table = [[1, 2, 3], [2, 3], [3], [], [1]]
    if is_cycle_present(adjacency_table, 5):
        handle_error()


def test_02():
    # Cycle 2->3->4->2
    adjacency_table = [[1, 2, 3], [2, 3], [3], [4], [2]]
    if not is_cycle_present(adjacency_table, 5):
        handle_error()


def main():
    test_01()
    test_02()
    print("Test passed")


if __name__ == "__main__":
    main()
