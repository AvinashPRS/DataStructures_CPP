def inorder_successor(root):
    """Returns the minimum node of a BST."""
    while root.left is not None:
        root = root.left
    return root


def bst_delete(root, node):
    """Deletes node from the BST; returns the new root."""
    parent = node.parent
    # No children or right-child only
    if node.left is None:
        if parent is not None and parent.left is node:
            parent.left = node.right
        elif parent is not None:
            parent.right = node.right
        if node.right is not None:
            node.right.parent = parent
        return node.right if parent is None else root
    # Left-child only
    if node.right is None:
        if parent is not None and parent.left is node:
            parent.left = node.left
        elif parent is not None:
            parent.right = node.left
        if node.left is not None:
            node.left.parent = parent
        return node.left if parent is None else root
    # Two children
    successor = inorder_successor(node.right)
    node.n = successor.n
    return bst_delete(root, successor)


def bst_remove_recursive(root, node, value):
    if node is not None:
        if node.n == value:
            return bst_delete(root, node)
        if node.n > value:
            return bst_remove_recursive(root, node.left, value)
        return bst_remove_recursive(root, node.right, value)
    return None


def bst_remove(root, value):
    """Removes value from a BST. A node with two children is replaced by its
    in-order successor. Returns the new root."""
    return bst_remove_recursive(root, root, value)
