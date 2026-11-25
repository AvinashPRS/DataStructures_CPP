def binary_tree_size(tree):
    """Measures the size (number of nodes) of a binary tree."""
    size = 0
    if tree:
        size += 1
        size += binary_tree_size(tree.left)
        size += binary_tree_size(tree.right)
    return size
