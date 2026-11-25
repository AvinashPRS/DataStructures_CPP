def binary_tree_sibling(node):
    """Finds the sibling of a node."""
    if node is None or node.parent is None:
        return None
    if node.parent.left is node:
        return node.parent.right
    return node.parent.left
