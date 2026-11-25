from binary_trees import (load, binary_tree_node,
                          binary_tree_rotate_left, binary_tree_rotate_right)

# The C project compiles this file together with 14-binary_tree_balance.c,
# whose binary_tree_height counts a leaf as 1.
binary_tree_height = load("14-binary_tree_balance").binary_tree_height


def height(tree):
    if tree is not None:
        l = 1 + binary_tree_height(tree.left) if tree.left else 1
        r = 1 + binary_tree_height(tree.right) if tree.right else 1
        return max(l, r)
    return 0


def balance(tree):
    return height(tree.left) - height(tree.right) if tree is not None else 0


def avl_insert_recursive(tree, parent, new, value):
    """tree: current subtree root, new: one-element list receiving the new
    node. Returns the (possibly rotated) subtree root, or None on failure."""
    if tree is None:
        new[0] = binary_tree_node(parent, value)
        return new[0]
    if tree.n > value:
        tree.left = avl_insert_recursive(tree.left, tree, new, value)
        if tree.left is None:
            return None
    elif tree.n < value:
        tree.right = avl_insert_recursive(tree.right, tree, new, value)
        if tree.right is None:
            return None
    else:
        return tree

    bfactor = balance(tree)
    if bfactor > 1 and tree.left.n > value:
        tree = binary_tree_rotate_right(tree)
    elif bfactor < -1 and tree.right.n < value:
        tree = binary_tree_rotate_left(tree)
    elif bfactor > 1 and tree.left.n < value:
        tree.left = binary_tree_rotate_left(tree.left)
        tree = binary_tree_rotate_right(tree)
    elif bfactor < -1 and tree.right.n > value:
        tree.right = binary_tree_rotate_right(tree.right)
        tree = binary_tree_rotate_left(tree)
    return tree


def avl_insert(tree, value):
    """Inserts value into an AVL tree.

    tree: one-element list holding the root. Returns the inserted node.
    """
    if tree is None:
        return None
    if tree[0] is None:
        tree[0] = binary_tree_node(None, value)
        return tree[0]
    new = [None]
    tree[0] = avl_insert_recursive(tree[0], tree[0], new, value)
    return new[0]
