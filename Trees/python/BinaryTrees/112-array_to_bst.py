from binary_trees import bst_insert


def array_to_bst(array, size=None):
    """Builds a BST from an array (duplicates are ignored)."""
    if array is None:
        return None
    if size is None:
        size = len(array)
    tree = [None]
    for i in range(size):
        if array[i] in array[:i]:
            continue
        if bst_insert(tree, array[i]) is None:
            return None
    return tree[0]
