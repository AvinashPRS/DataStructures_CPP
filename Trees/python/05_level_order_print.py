import sys
from collections import deque

from print_tree import print_tree

MAX_NUM_NODES_IN_TREE = 10


class Node:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


def handle_error():
    print("Test failed")
    sys.exit(1)


def construct_bst(parent, values, low, high):
    if low > high:
        return None
    middle = (low + high) // 2
    new_node = Node(values[middle], parent)
    new_node.left = construct_bst(new_node, values, low, middle - 1)
    new_node.right = construct_bst(new_node, values, middle + 1, high)
    return new_node


def print_data(data):
    print(data, end=" ")


def print_level_order(root, q):
    """Breadth first print, one level per line.
    q: queue (deque) that helps in printing in level order."""
    if root is None:
        return
    q.append(root)
    num_nodes_in_cur_level = 1
    num_nodes_in_next_level = 0
    while q:
        n = q.popleft()
        print_data(n.data)
        if n.left:
            q.append(n.left)
            num_nodes_in_next_level += 1
        if n.right:
            q.append(n.right)
            num_nodes_in_next_level += 1
        num_nodes_in_cur_level -= 1
        # go to next line if all nodes in current level are processed
        if num_nodes_in_cur_level == 0:
            print()
            num_nodes_in_cur_level = num_nodes_in_next_level
            num_nodes_in_next_level = 0


def main():
    q = deque()
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree")
        print_tree(root, num_elems)
        print("Level order is:")
        print_level_order(root, q)
        print("__________________________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
