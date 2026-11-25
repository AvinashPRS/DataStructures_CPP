def binary_tree_size(tree):
    if tree is None:
        return 0
    return binary_tree_size(tree.left) + binary_tree_size(tree.right) + 1


def tree_is_complete(tree, i, cnodes):
    if tree is None:
        return 1
    if i >= cnodes:
        return 0
    return int(tree_is_complete(tree.left, 2 * i + 1, cnodes) and
               tree_is_complete(tree.right, 2 * i + 2, cnodes))


def binary_tree_is_complete(tree):
    if tree is None:
        return 0
    return tree_is_complete(tree, 0, binary_tree_size(tree))


def check_parent(tree):
    """1 if no node in this subtree is greater than its parent."""
    if tree is None:
        return 1
    if tree.n > tree.parent.n:
        return 0
    return int(check_parent(tree.left) and check_parent(tree.right))


def binary_tree_is_heap(tree):
    """Checks if a binary tree is a valid Max Binary Heap."""
    if not binary_tree_is_complete(tree):
        return 0
    return int(check_parent(tree.left) and check_parent(tree.right))
