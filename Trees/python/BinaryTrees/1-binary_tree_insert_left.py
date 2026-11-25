from binary_trees import binary_tree_node


def binary_tree_insert_left(parent, value):
    """Inserts a node as the left-child of parent. If parent already has a
    left-child, the new node takes its place and the old left-child becomes
    the left-child of the new node."""
    if parent is None:
        return None
    new = binary_tree_node(parent, value)
    if parent.left is not None:
        new.left = parent.left
        parent.left.parent = new
    parent.left = new
    return new
