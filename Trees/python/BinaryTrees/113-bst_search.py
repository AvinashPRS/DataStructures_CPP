def bst_search(tree, value):
    """Searches for value in a BST; returns the node or None."""
    while tree is not None:
        if tree.n == value:
            return tree
        tree = tree.left if tree.n > value else tree.right
    return None
