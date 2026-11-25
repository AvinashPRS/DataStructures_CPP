from binary_trees import heap_insert


def array_to_heap(array, size=None):
    """Builds a Max Binary Heap tree from an array."""
    if array is None:
        return None
    if size is None:
        size = len(array)
    root = [None]
    for i in range(size):
        heap_insert(root, array[i])
    return root[0]
