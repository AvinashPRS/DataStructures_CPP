from binary_trees import binary_tree_node


def bst_insert(tree, value):
    """Inserts value in a BST.

    tree: one-element list holding the root (models bst_t **tree).
    Returns the created node, or None if value already exists.
    """
    if tree is None:
        return None
    curr = tree[0]
    if curr is None:
        tree[0] = binary_tree_node(None, value)
        return tree[0]
    while True:
        if value < curr.n:
            if curr.left is None:
                curr.left = binary_tree_node(curr, value)
                return curr.left
            curr = curr.left
        elif value > curr.n:
            if curr.right is None:
                curr.right = binary_tree_node(curr, value)
                return curr.right
            curr = curr.right
        else:
            return None
