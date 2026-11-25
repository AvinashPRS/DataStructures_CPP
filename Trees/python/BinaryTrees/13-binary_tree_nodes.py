def binary_tree_nodes(tree):
    """Counts the nodes with at least 1 child in a binary tree."""
    nodes = 0
    if tree:
        nodes += 1 if (tree.left or tree.right) else 0
        nodes += binary_tree_nodes(tree.left)
        nodes += binary_tree_nodes(tree.right)
    return nodes
