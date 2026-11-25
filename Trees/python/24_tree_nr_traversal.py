from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error

MAX_NUM_STACK_ELEMS = 10
MAX_VALUE = 10

nr_result_array = [0] * MAX_NUM_NODES_IN_TREE
nr_index = 0


def process(cur_node):
    global nr_index
    nr_result_array[nr_index] = cur_node.data
    nr_index += 1
    print(cur_node.data, end=" ")


def non_recursive_in_order(root, s):
    """Iterative in-order traversal using an explicit stack s (list)."""
    cur_node = root
    while cur_node or s:
        if cur_node:
            s.append(cur_node)          # push and go left
            cur_node = cur_node.left
        else:
            cur_node = s.pop()          # pop, process, go right
            process(cur_node)
            cur_node = cur_node.right


def recursive_in_order(node):
    global nr_index
    if node is None:
        return
    recursive_in_order(node.left)
    if nr_result_array[nr_index] != node.data:
        handle_error()
    nr_index += 1
    recursive_in_order(node.right)


def test_01():
    global nr_index
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    s = []
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root, num_elems)
        nr_index = 0
        print("Non Recursive In-order : ", end="")
        non_recursive_in_order(root, s)
        # verify against recursive in-order
        nr_index = 0
        recursive_in_order(root)
        print("\n__________________________________________________")
    print("Test passed")


if __name__ == "__main__":
    test_01()
