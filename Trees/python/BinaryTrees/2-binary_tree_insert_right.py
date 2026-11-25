from binary_trees import binary_tree_node


def binary_tree_insert_right(parent, value):
    """Inserts a node as the right-child of parent. If parent already has a
    right-child, the new node takes its place and the old right-child becomes
    the right-child of the new node."""
    if parent is None:
        return None
    new = binary_tree_node(parent, value)
    if parent.right is not None:
        new.right = parent.right
        parent.right.parent = new
    parent.right = new
    return new
