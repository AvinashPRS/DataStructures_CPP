def binary_tree_is_root(node):
    """Returns 1 if node is a root, otherwise 0."""
    if node is None or node.parent is not None:
        return 0
    return 1
