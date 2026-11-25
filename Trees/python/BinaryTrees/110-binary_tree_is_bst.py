INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1


def is_bst_helper(tree, lo, hi):
    if tree is not None:
        if tree.n < lo or tree.n > hi:
            return 0
        return int(is_bst_helper(tree.left, lo, tree.n - 1) and
                   is_bst_helper(tree.right, tree.n + 1, hi))
    return 1


def binary_tree_is_bst(tree):
    """Checks if a binary tree is a valid BST (no duplicates)."""
    if tree is None:
        return 0
    return is_bst_helper(tree, INT_MIN, INT_MAX)
