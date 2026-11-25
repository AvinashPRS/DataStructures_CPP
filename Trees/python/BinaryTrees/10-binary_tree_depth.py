def binary_tree_depth(tree):
    """Measures the depth of a node in a binary tree."""
    return 1 + binary_tree_depth(tree.parent) if (tree and tree.parent) else 0
