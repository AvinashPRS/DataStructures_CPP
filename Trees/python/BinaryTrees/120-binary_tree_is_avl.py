INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1


def height(tree):
    if tree:
        l = 1 + height(tree.left) if tree.left else 1
        r = 1 + height(tree.right) if tree.right else 1
        return max(l, r)
    return 0


def is_avl_helper(tree, lo, hi):
    if tree is not None:
        if tree.n < lo or tree.n > hi:
            return 0
        if abs(height(tree.left) - height(tree.right)) > 1:
            return 0
        return int(is_avl_helper(tree.left, lo, tree.n - 1) and
                   is_avl_helper(tree.right, tree.n + 1, hi))
    return 1


def binary_tree_is_avl(tree):
    """Checks if a binary tree is a valid AVL tree."""
    if tree is None:
        return 0
    return is_avl_helper(tree, INT_MIN, INT_MAX)
