def binary_tree_preorder(tree, func):
    """Goes through a binary tree using pre-order traversal."""
    if tree and func:
        func(tree.n)
        binary_tree_preorder(tree.left, func)
        binary_tree_preorder(tree.right, func)
