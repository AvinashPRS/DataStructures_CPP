def binary_tree_height(tree):
    """Height variant used for balance: a leaf has height 1, NULL has 0."""
    if tree:
        l = 1 + binary_tree_height(tree.left) if tree.left else 1
        r = 1 + binary_tree_height(tree.right) if tree.right else 1
        return max(l, r)
    return 0


def binary_tree_balance(tree):
    """Measures the balance factor of a binary tree."""
    if tree:
        return binary_tree_height(tree.left) - binary_tree_height(tree.right)
    return 0
