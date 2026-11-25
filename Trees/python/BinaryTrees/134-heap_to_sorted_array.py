from binary_trees import heap_extract, binary_tree_size


def heap_to_sorted_array(heap, size=None):
    """Converts a Max Binary Heap to an array sorted in descending order.

    The C version writes the length into *size; here `size` may be a
    one-element list to receive it. The array is returned.
    """
    if not heap:
        return None
    heap_size = binary_tree_size(heap)
    if size is not None:
        size[0] = heap_size
    array = []
    root = [heap]
    while root[0]:
        array.append(heap_extract(root))
    return array
