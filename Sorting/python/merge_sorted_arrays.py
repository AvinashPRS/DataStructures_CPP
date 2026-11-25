"""
Given two sorted arrays where the first has enough extra space at the back to hold the
second, merge them so the result (stored in the first array) is sorted.

Solution:
    Walk both arrays backwards from their last valid elements, writing the larger
    value at the back of the first array.

    TC: O(n + m)
    SC: O(1)
"""
import heapq


def merge_sorted_arrays(a, b, m, n):
    """Merges b (n elements) into a (m valid elements, room for m+n) from right to left."""
    i = m - 1               # last valid element in a
    j = n - 1               # last element in b
    write_idx = m + n - 1   # target write index at the end

    # Process backwards from the largest values
    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[write_idx] = a[i]
            i -= 1
        else:
            a[write_idx] = b[j]
            j -= 1
        write_idx -= 1

    # If a runs out first, copy the rest of b.
    # (If b runs out first, a's remaining elements are already in place.)
    while j >= 0:
        a[write_idx] = b[j]
        j -= 1
        write_idx -= 1

    return a


def merge_sorted_arrays_new(arr1, arr2):
    """Alternative: merge two sorted lists into a NEW sorted list."""
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


if __name__ == "__main__":
    a = [-22, 2, 5, 6]
    a.extend([0] * 6)  # Expand to fit elements of both arrays
    b = [-33, 0, 4, 5, 7, 8]

    merge_sorted_arrays(a, b, 4, 6)
    print("Merged array:", " ".join(map(str, a)))

    print("Merged Array:", " ".join(map(str, merge_sorted_arrays_new([1, 3, 5, 7], [2, 4, 6, 8, 10]))))

    # Python equivalent of std::merge
    print("heapq.merge :", " ".join(map(str, heapq.merge([1, 3, 5, 7], [2, 4, 6, 8, 10]))))
