def binary_tree_inorder(tree, func):
    """Goes through a binary tree using in-order traversal."""
    if tree and func:
        binary_tree_inorder(tree.left, func)
        func(tree.n)
        binary_tree_inorder(tree.right, func)
