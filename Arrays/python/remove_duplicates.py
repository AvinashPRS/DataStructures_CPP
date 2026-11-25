"""
Given a sorted array with duplicates, move the distinct numbers to the front of the
array and return the distinct numbers.

Solution:
    Two pointers: the current index and the write index. When the current element
    differs from its left neighbour, write it at the write index.

    TC: O(n)
    SC: O(1)
"""


def remove_duplicates(arr):
    if not arr:
        return []
    arr = list(arr)
    write_idx = 1
    for curr_idx in range(1, len(arr)):
        if arr[curr_idx] != arr[curr_idx - 1]:
            arr[write_idx] = arr[curr_idx]
            write_idx += 1
    return arr[:write_idx]


if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8]
    print(*remove_duplicates(arr))
