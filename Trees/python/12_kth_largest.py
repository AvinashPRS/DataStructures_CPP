from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error


def get_max(n):
    if n is None:
        return None
    while n.right:
        n = n.right
    return n


def get_previous(x):
    """In-order predecessor of x."""
    if x.left:
        return get_max(x.left)
    y = x.parent
    while y and y.left is x:
        x = y
        y = y.parent
    return y


def find_kth_largest(root, k):
    """Returns the kth largest node (k >= 1) of the BST, or None."""
    if root is None or k < 1:
        return None
    n = get_max(root)
    for _ in range(1, k):
        n = get_previous(n)
        if n is None:
            return None
    return n


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root1 = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root1, num_elems)
        for k in range(1, num_elems + 1):
            cur_node = find_kth_largest(root1, k)
            print("K = %d, Kth Largest = %d" % (k, cur_node.data))
            if cur_node.data != num_elems - k:
                handle_error()
        # k > num_elems must give None
        if find_kth_largest(root1, num_elems + 1) is not None:
            handle_error()
        print("_________________________________________________________")
    print("Test passed ")


if __name__ == "__main__":
    main()
