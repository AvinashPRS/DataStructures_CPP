"""Classic sorting algorithms: bubble, selection, insertion, quick, merge."""
import random


def bubble_sort(arr):
    """TC: O(n^2), best case O(n)"""
    arr = list(arr)
    n = len(arr)
    for i in range(n - 1):
        is_sorted = True  # reset at the start of every pass
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break
    return arr


def selection_sort(arr):
    """TC: O(n^2)"""
    arr = list(arr)
    for i in range(len(arr) - 1):
        min_el = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_el]:
                min_el = j
        arr[i], arr[min_el] = arr[min_el], arr[i]
    return arr


def insertion_sort(arr):
    """TC: O(n^2), best case O(n)"""
    arr = list(arr)
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


# ------------------------------ QUICK AND MERGE SORT ------------------------------
# Neither is universally "better": quicksort is the king of arrays and primitive data,
# mergesort is the king of linked lists, stable sorting and massive datasets.


def partition_array(arr, pivot_idx, l, h):
    """Partition helper for quicksort (Lomuto scheme)."""
    pivot_value = arr[pivot_idx]
    arr[h], arr[pivot_idx] = arr[pivot_idx], arr[h]
    small = l

    for i in range(l, h):
        if arr[i] < pivot_value:
            arr[i], arr[small] = arr[small], arr[i]
            small += 1
    arr[h], arr[small] = arr[small], arr[h]
    return small


def _quick_sort_helper(arr, l, h):
    if l < h:
        pivot_idx = random.randint(l, h)
        partition_idx = partition_array(arr, pivot_idx, l, h)
        _quick_sort_helper(arr, l, partition_idx - 1)
        _quick_sort_helper(arr, partition_idx + 1, h)


def quick_sort(arr):
    """TC: average O(n log n), worst O(n^2)"""
    arr = list(arr)
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def merge_arrays(arr, l, mid, h):
    """Merges arr[l..mid] and arr[mid+1..h]."""
    L = arr[l:mid + 1]
    R = arr[mid + 1:h + 1]

    i = j = 0
    k = l
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    arr[k:h + 1] = L[i:] + R[j:]


def _merge_sort_helper(arr, l, h):
    if l < h:
        mid = l + (h - l) // 2
        _merge_sort_helper(arr, l, mid)
        _merge_sort_helper(arr, mid + 1, h)
        merge_arrays(arr, l, mid, h)


def merge_sort(arr):
    """TC: O(n log n), SC: O(n). Better than quicksort for the worst case."""
    arr = list(arr)
    _merge_sort_helper(arr, 0, len(arr) - 1)
    return arr


def fmt(arr):
    return "".join(f"{d} " for d in arr)


if __name__ == "__main__":
    arr = [0, -2, -3, 6, 3, 2, 17, 2, 7, -4, 9]

    print("Original:\n" + fmt(arr))
    print("Bubble Sort:\n" + fmt(bubble_sort(arr)))
    print("Selection Sort:\n" + fmt(selection_sort(arr)))
    print("Insertion Sort:\n" + fmt(insertion_sort(arr)))
    print("Quick Sort:\n" + fmt(quick_sort(arr)))
    print("Merge Sort:\n" + fmt(merge_sort(arr)))
