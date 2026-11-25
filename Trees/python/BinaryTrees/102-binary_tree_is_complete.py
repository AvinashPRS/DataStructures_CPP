def binary_tree_is_leaf(node):
    return 1 if (node is not None and node.left is None and node.right is None) else 0


def binary_tree_height(tree):
    """Height counting nodes (NULL -> 0, leaf -> 1)."""
    if tree is None:
        return 0
    return 1 + max(binary_tree_height(tree.left), binary_tree_height(tree.right))


def binary_tree_is_perfect(tree):
    if tree is None:
        return 1
    l, r = tree.left, tree.right
    if binary_tree_is_leaf(tree):
        return 1
    if l is None or r is None:
        return 0
    if binary_tree_height(l) == binary_tree_height(r):
        if binary_tree_is_perfect(l) and binary_tree_is_perfect(r):
            return 1
    return 0


def binary_tree_is_complete(tree):
    """Checks if a binary tree is complete."""
    if tree is None:
        return 0
    if binary_tree_is_leaf(tree):
        return 1
    l, r = tree.left, tree.right
    l_height = binary_tree_height(l)
    r_height = binary_tree_height(r)
    if l_height == r_height:
        if binary_tree_is_perfect(l) and binary_tree_is_complete(r):
            return 1
    elif l_height == r_height + 1:
        if binary_tree_is_complete(l) and binary_tree_is_perfect(r):
            return 1
    return 0
