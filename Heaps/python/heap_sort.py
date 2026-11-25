"""
Heap sort.
    TC: O(n log n) in all cases (best, worst, average)
    SC: O(1)
"""
import heapq


def heapify(arr, n, i):
    """Heapify a subtree rooted at index i; n is the size of the heap."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying the affected sub-tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: One by one extract an element from the heap.
    # Building the max heap only guarantees the largest element is at the root;
    # the rest is only partially ordered, so we repeatedly move the root to the end.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def print_array(arr):
    print(" ".join(str(x) for x in arr))


def heap_sort_stdlib(arr):
    """Alternative using Python's heapq (min-heap)."""
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array: ", end="")
    print_array(arr)

    heap_sort(arr)

    print("Sorted array:   ", end="")
    print_array(arr)

    print("heapq approach: ", end="")
    print_array(heap_sort_stdlib([12, 11, 13, 5, 6, 7]))
