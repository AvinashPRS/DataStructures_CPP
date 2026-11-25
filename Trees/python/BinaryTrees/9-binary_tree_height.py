def binary_tree_height(tree):
    """Measures the height of a binary tree (edges). NULL / leaf -> 0."""
    if tree:
        l = 1 + binary_tree_height(tree.left) if tree.left else 0
        r = 1 + binary_tree_height(tree.right) if tree.right else 0
        return max(l, r)
    return 0
