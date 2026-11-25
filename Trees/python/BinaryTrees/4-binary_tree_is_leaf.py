def binary_tree_is_leaf(node):
    """Returns 1 if node is a leaf, otherwise 0."""
    if node is None or node.left is not None or node.right is not None:
        return 0
    return 1
