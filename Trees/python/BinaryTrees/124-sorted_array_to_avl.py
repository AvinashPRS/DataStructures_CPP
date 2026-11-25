from binary_trees import BinaryTreeNode


def _sorted_array_to_avl(array, start, end, parent):
    if start > end:
        return None
    mid = (start + end) // 2
    new = BinaryTreeNode(array[mid], parent)
    new.left = _sorted_array_to_avl(array, start, mid - 1, new)
    new.right = _sorted_array_to_avl(array, mid + 1, end, new)
    return new


def sorted_array_to_avl(array, size=None):
    """Builds an AVL tree from a sorted array."""
    if not array:
        return None
    if size is None:
        size = len(array)
    return _sorted_array_to_avl(array, 0, size - 1, None)
