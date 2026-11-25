def binary_tree_delete(tree):
    """Deletes a binary tree (unlinks every node; the GC frees memory)."""
    if tree is not None:
        binary_tree_delete(tree.left)
        binary_tree_delete(tree.right)
        tree.left = tree.right = tree.parent = None
