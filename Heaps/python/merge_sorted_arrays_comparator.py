"""
Merge multiple sorted lists using a min-heap of iterators.

C++ stores (curr, last) iterator pairs in the heap with a lambda comparator.
In Python we store (current_value, list_index, iterator) - list_index breaks
ties so iterators themselves are never compared.
"""
import heapq


def merge_multiple_sorted_vectors(arr):
    sorted_list = []
    min_heap = []

    # push only non-empty lists
    for idx, a in enumerate(arr):
        it = iter(a)
        first = next(it, None)
        if first is not None:
            min_heap.append((first, idx, it))
    heapq.heapify(min_heap)

    # pop the smallest and advance that list's iterator
    while min_heap:
        value, idx, it = min_heap[0]
        sorted_list.append(value)

        nxt = next(it, None)
        if nxt is not None:
            heapq.heapreplace(min_heap, (nxt, idx, it))
        else:
            heapq.heappop(min_heap)

    return sorted_list


if __name__ == "__main__":
    arrays = [
        [1, 5, 9, 21],
        [2, 6, 12],
        [0, 3, 7, 15, 30],
        [],     # empty list is safely ignored
    ]
    result = merge_multiple_sorted_vectors(arrays)
    print("Merged Output: " + " ".join(str(n) for n in result))
