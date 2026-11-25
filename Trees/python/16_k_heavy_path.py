from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error

MAX_NODE_VALUE = 10


def k_heavy_path(cur_node, above_sum, k):
    """Remove all nodes that don't lie on a root-to-leaf path whose sum >= k.

    above_sum: sum of nodes from root to parent of cur_node
    Returns: the largest root-to-leaf path sum through cur_node
    """
    if cur_node is None:
        return above_sum
    above_sum += cur_node.data

    max_left_path = k_heavy_path(cur_node.left, above_sum, k)
    if max_left_path < k:  # prune left subtree
        cur_node.left = None

    max_right_path = k_heavy_path(cur_node.right, above_sum, k)
    if max_right_path < k:  # prune right subtree
        cur_node.right = None

    return max(max_left_path, max_right_path)


def verify_path(cur_node, top_sum, K):
    """Verify all root-to-leaf paths have sum >= K."""
    if cur_node is None:
        return top_sum
    top_sum += cur_node.data
    max_left_path = verify_path(cur_node.left, top_sum, K)
    max_right_path = verify_path(cur_node.right, top_sum, K)
    if max_left_path < K and max_right_path < K:
        handle_error()
    return max(max_left_path, max_right_path)


def test():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root = construct_bst(None, number_array, 0, num_elems - 1)
        print("Original tree:")
        print_tree(root, num_elems)
        K = 20
        # if no root-to-leaf path has sum >= K the root itself is removed
        if k_heavy_path(root, 0, K) < K:
            root = None
        print("After retaining only K-Heavy paths (K = %d):" % K)
        print_tree(root, num_elems)
        verify_path(root, 0, K)
        print("___________________________________________________")


def main():
    test()
    print("Test passed ")


if __name__ == "__main__":
    main()
