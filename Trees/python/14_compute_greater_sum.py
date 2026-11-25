from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error


def compute_sum_of_greater_nodes(cur_node, sum_p):
    """Reverse in-order walk: store in each node the sum of all greater nodes.
    sum_p: one-element list holding the running sum."""
    if cur_node is None:
        return
    # greater elements are in the right subtree -> process it first
    compute_sum_of_greater_nodes(cur_node.right, sum_p)
    cur_node.sum = sum_p[0]
    sum_p[0] += cur_node.data
    compute_sum_of_greater_nodes(cur_node.left, sum_p)


def verify_sum(cur_node, sum_array, index_p):
    if cur_node is None:
        return
    verify_sum(cur_node.left, sum_array, index_p)
    print("Node data = %d, Greater sum =%d" % (cur_node.data, cur_node.sum))
    if sum_array[index_p[0]] != cur_node.sum:
        handle_error("Error occured while comparing tree and sum array")
    index_p[0] += 1
    verify_sum(cur_node.right, sum_array, index_p)


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    sum_array = [0] * MAX_NUM_NODES_IN_TREE
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root, num_elems)

        compute_sum_of_greater_nodes(root, [0])

        sum_so_far = 0
        for i in range(num_elems - 1, -1, -1):
            sum_array[i] = sum_so_far
            sum_so_far += number_array[i]

        verify_sum(root, sum_array, [0])
        print("___________________________________________________")
    print("Test passed ")


if __name__ == "__main__":
    main()
