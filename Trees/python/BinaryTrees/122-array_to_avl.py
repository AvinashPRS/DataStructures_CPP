from binary_trees import avl_insert


def array_to_avl(array, size=None):
    """Builds an AVL tree from an array (duplicates are ignored)."""
    if array is None:
        return None
    if size is None:
        size = len(array)
    tree = [None]
    for i in range(size):
        if array[i] in array[:i]:
            continue
        if avl_insert(tree, array[i]) is None:
            return None
    return tree[0]
