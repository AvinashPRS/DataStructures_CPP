def binary_tree_leaves(tree):
    """Counts the leaves in a binary tree."""
    leaves = 0
    if tree:
        leaves += 1 if (not tree.left and not tree.right) else 0
        leaves += binary_tree_leaves(tree.left)
        leaves += binary_tree_leaves(tree.right)
    return leaves
