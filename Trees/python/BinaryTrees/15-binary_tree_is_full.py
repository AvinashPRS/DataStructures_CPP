def is_full_recursive(tree):
    if tree is not None:
        if ((tree.left is not None and tree.right is None) or
                (tree.left is None and tree.right is not None) or
                is_full_recursive(tree.left) == 0 or
                is_full_recursive(tree.right) == 0):
            return 0
    return 1


def binary_tree_is_full(tree):
    """Checks if a binary tree is full (every node has 0 or 2 children)."""
    if tree is None:
        return 0
    return is_full_recursive(tree)
