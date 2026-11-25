from print_tree import print_tree
from tree_common import MAX_NUM_NODES_IN_TREE, construct_bst, handle_error


def get_max(n):
    """The rightmost node has the maximum value."""
    if n is None:
        return None
    while n.right:
        n = n.right
    return n


def get_previous(x):
    """In-order predecessor of node x (uses parent pointers)."""
    # Case 1: left child exists -> max of left subtree
    if x.left:
        y = x.left
        while y.right:
            y = y.right
        return y
    # Case 2: go up until we come from a right child
    y = x.parent
    while y and y.left is x:
        x = y
        y = y.parent
    return y


def get_next(x):
    """In-order successor of node x (uses parent pointers)."""
    # Case 1: right child exists -> min of right subtree
    if x.right:
        y = x.right
        while y.left:
            y = y.left
        return y
    # Case 2: go up until we come from a left child
    y = x.parent
    while y and y.right is x:
        x = y
        y = y.parent
    return y


def node_str(n):
    return str(n.data) if n else "NULL"


def verify_previous_next(cur_node, num_elems):
    if cur_node is None:
        return
    prev_node = get_previous(cur_node)
    next_node = get_next(cur_node)
    print("Cur node = %s: Prev node = %s, Next node = %s" %
          (node_str(cur_node), node_str(prev_node), node_str(next_node)))

    if cur_node.data == 0:
        if prev_node is not None:
            handle_error()
    elif prev_node.data + 1 != cur_node.data:
        handle_error()

    if cur_node.data == num_elems - 1:
        if next_node is not None:
            handle_error()
    elif cur_node.data + 1 != next_node.data:
        handle_error()

    verify_previous_next(cur_node.left, num_elems)
    verify_previous_next(cur_node.right, num_elems)


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        root1 = construct_bst(None, number_array, 0, num_elems - 1)
        print("Printing tree:")
        print_tree(root1, num_elems)
        verify_previous_next(root1, num_elems)
        print("____________________________________________________")
    print("Test passed")


if __name__ == "__main__":
    main()
