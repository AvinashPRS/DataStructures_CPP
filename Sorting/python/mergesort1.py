"""
Merge sort on a list.

- Time Complexity: O(n log n) in all cases (array always split evenly, linear merge).
- Space Complexity: O(n) for the temporary sub-lists created during merge.
- Stability: stable; equal elements keep their relative order.
"""


def merge(arr, left, mid, right):
    """Merges two sorted sub-ranges arr[left..mid] and arr[mid+1..right]."""
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L, if any
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R, if any
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def print_array(arr):
    print("".join(f"{x} " for x in arr))


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("Original array: ", end="")
    print_array(arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("Sorted array:   ", end="")
    print_array(arr)
