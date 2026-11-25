"""K&R-style quicksort: sort v[left]..v[right] into increasing order."""


def swap(v, i, j):
    """Interchange v[i] and v[j]."""
    v[i], v[j] = v[j], v[i]


def qsort(v, left, right):
    if left >= right:                      # do nothing if fewer than two elements
        return
    swap(v, left, (left + right) // 2)     # move partition element to v[left]
    last = left
    for i in range(left + 1, right + 1):   # partition
        if v[i] < v[left]:
            last += 1                      # increment last, not left
            swap(v, last, i)

    swap(v, left, last)                    # restore partition element
    qsort(v, left, last - 1)
    qsort(v, last + 1, right)


if __name__ == "__main__":
    arr = [34, -10, 5, 0, 100, 2, 89, -5, 23]

    print("Original array:")
    print(" ".join(map(str, arr)))
    print()

    qsort(arr, 0, len(arr) - 1)

    print("Sorted array:")
    print(" ".join(map(str, arr)))
