import sys

from print_tree import print_tree

MAX_NUM_NODES_IN_TREE = 10


class Node:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.depth = parent.depth + 1 if parent else 0
        self.left = None
        self.right = None
        self.parent = parent
        self.next = None


def construct_bst(parent, values, low, high):
    if low > high:
        return None
    middle = (low + high) // 2
    new_node = Node(values[middle], parent)
    new_node.left = construct_bst(new_node, values, low, middle - 1)
    new_node.right = construct_bst(new_node, values, middle + 1, high)
    return new_node


def handle_error():
    print("Test failed")
    sys.exit(1)


def swap_children(cur_node):
    if cur_node is None:
        return
    cur_node.left, cur_node.right = cur_node.right, cur_node.left
    swap_children(cur_node.left)
    swap_children(cur_node.right)


def is_bst(cur_node, prev_node):
    """In-order check.
    prev_node: one-element list holding the in-order predecessor
               (plays the role of the C double pointer).
    Returns 1 if the tree is a BST, 0 otherwise."""
    if cur_node is None:
        return 1
    if not is_bst(cur_node.left, prev_node):
        return 0
    if prev_node[0] is not None and cur_node.data <= prev_node[0].data:
        return 0
    prev_node[0] = cur_node
    return is_bst(cur_node.right, prev_node)


def print_result(result):
    if result:
        print("The tree is a Binary Search Tree\n\n")
    else:
        print("The tree is NOT a Binary Search Tree\n")


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree")
        print_tree(root, num_elems)

        result = is_bst(root, [None])
        print_result(result)
        if not result:
            handle_error()

        # after swapping children it must no longer be a BST (if > 1 node)
        swap_children(root)
        print("Printing tree:")
        print_tree(root, num_elems)
        result = is_bst(root, [None])
        print_result(result)
        if result and num_elems > 1:
            handle_error()
        print("_____________________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
