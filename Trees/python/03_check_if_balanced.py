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


def construct_bst(parent, values, low, high):
    if low > high:
        return None
    middle = (low + high) // 2
    new_node = Node(values[middle], parent)
    new_node.left = construct_bst(new_node, values, low, middle - 1)
    new_node.right = construct_bst(new_node, values, middle + 1, high)
    return new_node


def construct_unbalanced_tree(num_nodes):
    """Builds a right-skewed chain 0 -> 1 -> 2 ..."""
    root = prev_node = None
    for i in range(num_nodes):
        new_node = Node(i)
        if root is None:
            root = new_node
        if prev_node:
            prev_node.right = new_node
        prev_node = new_node
    return root


def print_unbalanced_tree(root):
    count = 0
    cur_node = root
    while cur_node:
        print("\t" * count + str(cur_node.data))
        count += 1
        cur_node = cur_node.right


def handle_error():
    print("Test failed")
    sys.exit(1)


def is_balanced(cur_node):
    """Returns (is_balanced, height) for the subtree rooted at cur_node."""
    if cur_node is None:
        return 1, 0
    is_left_balanced, left_height = is_balanced(cur_node.left)
    is_right_balanced, right_height = is_balanced(cur_node.right)
    if not is_left_balanced or not is_right_balanced:
        return 0, 0
    # height difference of more than 1 -> unbalanced
    if abs(left_height - right_height) > 1:
        return 0, 0
    return 1, max(left_height, right_height) + 1


def print_result(result):
    if result:
        print("The tree is balanced\n\n")
    else:
        print("The tree is NOT balanced\n")


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))

    # balanced trees
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree")
        print_tree(root, num_elems)
        result, _ = is_balanced(root)
        print_result(result)
        if result != 1:
            handle_error()
        print("_____________________________________________________")

    # unbalanced trees
    for num_elems in range(3, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_unbalanced_tree(num_elems)
        print_unbalanced_tree(root)
        result, _ = is_balanced(root)
        print_result(result)
        if result != 0:
            handle_error()
        print("_____________________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
