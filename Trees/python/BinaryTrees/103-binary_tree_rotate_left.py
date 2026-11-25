def binary_tree_rotate_left(tree):
    """Left-rotates a binary tree; returns the new root of the subtree."""
    if tree is None or tree.right is None:
        return None
    pivot = tree.right
    tmp = pivot.left
    pivot.left = tree
    tree.right = tmp
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
