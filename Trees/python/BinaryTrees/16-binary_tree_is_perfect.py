def is_leaf(node):
    return 1 if (node.left is None and node.right is None) else 0


def depth(tree):
    return 1 + depth(tree.parent) if tree.parent is not None else 0


def get_leaf(tree):
    """Returns the first encountered leaf."""
    if is_leaf(tree) == 1:
        return tree
    return get_leaf(tree.left) if tree.left else get_leaf(tree.right)


def is_perfect_recursive(tree, leaf_depth, level):
    if is_leaf(tree):
        return 1 if level == leaf_depth else 0
    if tree.left is None or tree.right is None:
        return 0
    return int(is_perfect_recursive(tree.left, leaf_depth, level + 1) and
               is_perfect_recursive(tree.right, leaf_depth, level + 1))


def binary_tree_is_perfect(tree):
    """Checks if a binary tree is perfect."""
    if tree is None:
        return 0
    return is_perfect_recursive(tree, depth(get_leaf(tree)), 0)
