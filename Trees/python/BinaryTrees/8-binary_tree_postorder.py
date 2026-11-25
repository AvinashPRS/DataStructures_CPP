def binary_tree_postorder(tree, func):
    """Goes through a binary tree using post-order traversal."""
    if tree and func:
        binary_tree_postorder(tree.left, func)
        binary_tree_postorder(tree.right, func)
        func(tree.n)
