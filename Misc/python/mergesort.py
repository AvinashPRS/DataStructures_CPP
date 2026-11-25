"""Merge sort (top-down)."""


def merge(arr, left, mid, right):
    """Merge sorted arr[left..mid] and arr[mid+1..right]; mid is the partition."""
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
    # consume the remaining elements
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
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


def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array: " + "".join(f"{x} " for x in arr))


if __name__ == "__main__":
    main()
