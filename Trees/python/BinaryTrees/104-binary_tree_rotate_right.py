def binary_tree_rotate_right(tree):
    """Right-rotates a binary tree; returns the new root of the subtree."""
    if tree is None or tree.left is None:
        return None
    pivot = tree.left
    tmp = pivot.right
    pivot.right = tree
    tree.left = tmp
    if tmp is not None:
        tmp.parent = tree
    tmp = tree.parent
    tree.parent = pivot
    pivot.parent = tmp
    if tmp is not None:
        if tmp.left is tree:
            tmp.left = pivot
        else:
            tmp.right = pivot
    return pivot
