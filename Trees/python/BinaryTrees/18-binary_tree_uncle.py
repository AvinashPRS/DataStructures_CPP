def binary_tree_uncle(node):
    """Finds the uncle of a node."""
    if node is None or node.parent is None or node.parent.parent is None:
        return None
    if node.parent.parent.left is node.parent:
        return node.parent.parent.right
    return node.parent.parent.left
