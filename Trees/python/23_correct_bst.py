import random

from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error, is_bst


def find_error_nodes(cur_node, prev_node, errors):
    """In-order walk that finds the two swapped nodes of a BST.
    prev_node: one-element list - in-order predecessor of cur_node
    errors: two-element list [error1, error2] receiving the error nodes
    """
    if cur_node is None:
        return
    find_error_nodes(cur_node.left, prev_node, errors)
    # cur_node should be greater than the previous node
    if prev_node[0] is not None and cur_node.data <= prev_node[0].data:
        if errors[0] is None:
            errors[0] = prev_node[0]
            errors[1] = cur_node
        else:
            errors[1] = cur_node
            return
    prev_node[0] = cur_node
    find_error_nodes(cur_node.right, prev_node, errors)


def correct_bst(root):
    """Fix a BST in which the data of two nodes has been swapped."""
    errors = [None, None]
    find_error_nodes(root, [None], errors)
    if errors[0] is not None and errors[1] is not None:
        errors[0].data, errors[1].data = errors[1].data, errors[0].data


def main():
    for num_elems in range(2, MAX_NUM_NODES_IN_TREE + 1):
        number_array = list(range(num_elems))
        index1 = random.randrange(num_elems)
        index2 = random.randrange(num_elems)
        print("Num elements = %d, Swapping node at %d with node at %d \n" %
              (num_elems, index1, index2))
        number_array[index1], number_array[index2] = number_array[index2], number_array[index1]

        # two wrong positions in the array -> two wrong nodes in the BST
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing the Incorrect tree: ")
        print_tree(root, num_elems)

        correct_bst(root)
        print("Printing the Corrected tree: ")
        print_tree(root, num_elems)

        if not is_bst(root, [None]):
            handle_error("Error occured")
        print("______________________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
