from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, check_condition


def get_previous(x):
    """In-order predecessor of x."""
    if x.left:
        y = x.left
        while y.right:
            y = y.right
        return y
    y = x.parent
    while y and y.left is x:
        x = y
        y = y.parent
    return y


def get_next(x):
    """In-order successor of x."""
    if x.right:
        y = x.right
        while y.left:
            y = y.left
        return y
    y = x.parent
    while y and y.right is x:
        x = y
        y = y.parent
    return y


def find_pair_sum_to_k(root, k):
    """Find two nodes in the BST whose data sums to k.
    Returns (node1, node2) or (None, None)."""
    if root is None:
        return None, None
    # leftmost (smallest) node
    n1 = root
    while n1.left:
        n1 = n1.left
    # rightmost (largest) node
    n2 = root
    while n2.right:
        n2 = n2.right
    # two-pointer walk from both ends
    while n1 is not n2:
        s = n1.data + n2.data
        if s == k:
            return n1, n2
        if s < k:
            n1 = get_next(n1)
        else:
            n2 = get_previous(n2)
    return None, None


def find_array_sum_to_k(number_array, num_elems, k):
    """Brute force on the array. Returns (val1, val2) or (-1, -1)."""
    for i in range(num_elems - 1):
        for j in range(num_elems - 1, i, -1):
            if number_array[i] + number_array[j] == k:
                return number_array[i], number_array[j]
    return -1, -1


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root1 = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root1, num_elems)
        for K in range(2 * num_elems + 1):
            n1, n2 = find_pair_sum_to_k(root1, K)
            num1, num2 = find_array_sum_to_k(number_array, num_elems, K)
            # the result from the tree and the array should match
            if n1 is None or num1 == -1:
                check_condition(n1 is None)
                check_condition(n2 is None)
                check_condition(num1 == -1)
                check_condition(num2 == -1)
            else:
                check_condition(n1.data == num1)
                check_condition(n2.data == num2)
                print("%d + %d = %d" % (n1.data, n2.data, K))
        print("__________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
