"""Heap sort using a max-heap.

Note: the C++ version computes the right child as `2 * 1 + 2` (typo);
the correct `2 * i + 2` is used here.
"""


def heapify(arr, n, i):
    """Maintain the max-heap property for the subtree rooted at i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Step 1: build a max-heap, starting from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Step 2: move the root (largest) to the end and restore the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def main():
    arr = [10, 5, 20, 2, 15]
    heap_sort(arr)
    print("Sorted Array: " + "".join(f"{v} " for v in arr))


if __name__ == "__main__":
    main()
