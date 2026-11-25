import sys

from print_tree import print_tree

MAX_NUM_NODES_IN_TREE = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


class Node:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


def construct_bst(parent, values, low, high):
    """Recursively construct a BST from a sorted array."""
    if low > high:
        return None
    middle = (low + high) // 2
    new_node = Node(values[middle], parent)
    new_node.left = construct_bst(new_node, values, low, middle - 1)
    new_node.right = construct_bst(new_node, values, middle + 1, high)
    return new_node


def compute_mirror_image(cur_node):
    """Swap left and right children of every node."""
    if cur_node:
        cur_node.left, cur_node.right = cur_node.right, cur_node.left
        compute_mirror_image(cur_node.left)
        compute_mirror_image(cur_node.right)


def compare_nodes(n1, n2):
    if n1 is None and n2 is None:  # both NULL -> symmetric
        return 1
    if n1 is None or n2 is None:  # only one NULL -> not symmetric
        return 0
    if n1.data != n2.data:
        return 0
    if not compare_nodes(n1.left, n2.right):
        return 0
    if not compare_nodes(n1.right, n2.left):
        return 0
    return 1


def is_symmetric(root):
    """Returns 1 if the tree is symmetric, 0 otherwise."""
    if root is None:
        return 1
    return compare_nodes(root.left, root.right)


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    main_root = Node()
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root1 = construct_bst(None, number_array, 0, num_elems - 1)
        root2 = construct_bst(None, number_array, 0, num_elems - 1)
        print("Original tree: ")
        print_tree(root1, num_elems)

        compute_mirror_image(root2)
        print("Mirror image: ")
        print_tree(root2, num_elems)

        # root1 and root2 are mirror images, so a root holding them as its
        # children must be symmetric
        main_root.left = root1
        main_root.right = root2
        if not is_symmetric(main_root):
            handle_error()
        print("_____________________________________________________________")
    print("Test passed ")


if __name__ == "__main__":
    main()
