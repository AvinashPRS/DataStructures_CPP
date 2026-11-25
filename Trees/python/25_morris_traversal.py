from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error

MAX_VALUE = 10

morris_result_array = [0] * MAX_NUM_NODES_IN_TREE
morris_index = 0


def print_morris(cur_node):
    global morris_index
    print(cur_node.data, end=" ")
    morris_result_array[morris_index] = cur_node.data
    morris_index += 1


def morris_traversal(root):
    """In-order traversal in O(1) extra space using temporary threads."""
    cur_node = root
    while cur_node:
        # no left subtree: process and go right
        if cur_node.left is None:
            print_morris(cur_node)
            cur_node = cur_node.right
            continue

        # find in-order predecessor (rightmost node of left subtree)
        left_pre = cur_node.left
        while left_pre.right is not None and left_pre.right is not cur_node:
            left_pre = left_pre.right

        if left_pre.right is None:
            # left subtree not visited yet: create thread and go left
            left_pre.right = cur_node
            cur_node = cur_node.left
        else:
            # left subtree done: remove thread, process, go right
            left_pre.right = None
            print_morris(cur_node)
            cur_node = cur_node.right


def recursive_in_order(node):
    global morris_index
    if node is None:
        return
    recursive_in_order(node.left)
    if morris_result_array[morris_index] != node.data:
        handle_error()
    morris_index += 1
    recursive_in_order(node.right)


def test_01():
    global morris_index
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root, num_elems)
        print("Morris In-order : ", end="")
        morris_index = 0
        morris_traversal(root)
        morris_index = 0
        recursive_in_order(root)
        print("\n___________________________________________")
    print("Test passed")


if __name__ == "__main__":
    test_01()
