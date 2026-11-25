from binary_trees import (binary_tree_balance, binary_tree_rotate_left,
                          binary_tree_rotate_right)


def bal(tree):
    """Rebalances every subtree (post-order). Returns the new subtree root."""
    if tree is None:
        return None
    if tree.left is None and tree.right is None:
        return tree
    tree.left = bal(tree.left)
    tree.right = bal(tree.right)
    bval = binary_tree_balance(tree)
    if bval > 1:
        tree = binary_tree_rotate_right(tree)
    elif bval < -1:
        tree = binary_tree_rotate_left(tree)
    return tree


def successor(node):
    """Value of the minimum node in the subtree (0 if empty)."""
    if node is None:
        return 0
    left = successor(node.left)
    return node.n if left == 0 else left


def remove_type(root):
    """Removes a node depending on its children.
    Returns 0 if it was unlinked, else the successor value copied into it."""
    if not root.left and not root.right:
        if root.parent.right is root:
            root.parent.right = None
        else:
            root.parent.left = None
        return 0
    elif (not root.left and root.right) or (not root.right and root.left):
        if not root.left:
            if root.parent.right is root:
                root.parent.right = root.right
            else:
                root.parent.left = root.right
            root.right.parent = root.parent
        if not root.right:
            if root.parent.right is root:
                root.parent.right = root.left
            else:
                root.parent.left = root.left
            root.left.parent = root.parent
        return 0
    else:
        new_value = successor(root.right)
        root.n = new_value
        return new_value


def bst_remove(root, value):
    """Removes a node from a BST."""
    if root is None:
        return None
    if value < root.n:
        bst_remove(root.left, value)
    elif value > root.n:
        bst_remove(root.right, value)
    else:
        t = remove_type(root)
        if t != 0:
            bst_remove(root.right, t)
    return root


def avl_remove(root, value):
    """Removes a node from an AVL tree; returns the new root."""
    root_a = bst_remove(root, value)
    if root_a is None:
        return None
    return bal(root_a)
