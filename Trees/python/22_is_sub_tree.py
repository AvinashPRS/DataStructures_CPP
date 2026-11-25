from tree_common import MAX_NUM_NODES_IN_TREE, Node, construct_bst, handle_error

INVALID_VALUE = 100


def compare_nodes(n1, n2):
    """1 if subtree at n1 (main tree) matches subtree at n2 exactly."""
    if n1 is None and n2 is None:
        return 1
    if n1 is None or n2 is None:
        return 0
    if n1.data != n2.data:
        return 0
    return int(compare_nodes(n1.left, n2.left) and compare_nodes(n1.right, n2.right))


def is_sub_tree(root1, root2):
    """1 if tree under root2 is present in tree under root1."""
    if root2 is None:  # empty tree is a sub-tree of every tree
        return 1
    if root1 is None:
        return 0
    if compare_nodes(root1, root2):
        return 1
    return int(is_sub_tree(root1.left, root2) or is_sub_tree(root1.right, root2))


def main():
    number_array = list(range(MAX_NUM_NODES_IN_TREE))
    err = "Error occured"
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        sub_tree_root = construct_bst(None, number_array, 0, num_elems - 1)
        main_tree_root = Node(INVALID_VALUE)

        # main root has an invalid value -> sub-tree must not be found
        if is_sub_tree(main_tree_root, sub_tree_root):
            handle_error(err)

        main_tree_root.left, main_tree_root.right = sub_tree_root, None
        if not is_sub_tree(main_tree_root, sub_tree_root):
            handle_error(err)

        main_tree_root.left, main_tree_root.right = None, sub_tree_root
        if not is_sub_tree(main_tree_root, sub_tree_root):
            handle_error(err)

        if not is_sub_tree(sub_tree_root, sub_tree_root):
            handle_error(err)
        if not is_sub_tree(main_tree_root, None):
            handle_error(err)
        if is_sub_tree(None, sub_tree_root):
            handle_error(err)
    print("Test passed")


if __name__ == "__main__":
    main()
