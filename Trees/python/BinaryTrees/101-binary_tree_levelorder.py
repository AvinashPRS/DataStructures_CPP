def binary_tree_height(tree):
    """Height counting nodes (NULL -> 0, leaf -> 1)."""
    if tree is None:
        return 0
    return 1 + max(binary_tree_height(tree.left), binary_tree_height(tree.right))


def binary_tree_level(tree, l, func):
    """Performs func on every node at level l (root is level 1)."""
    if tree is None:
        return
    if l == 1:
        func(tree.n)
    elif l > 1:
        binary_tree_level(tree.left, l - 1, func)
        binary_tree_level(tree.right, l - 1, func)


def binary_tree_levelorder(tree, func):
    """Traverses a binary tree using level-order traversal."""
    if tree is None or func is None:
        return
    for i in range(1, binary_tree_height(tree) + 1):
        binary_tree_level(tree, i, func)
