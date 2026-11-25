"""
Given an array where each entry stores the max steps that can be taken from there,
find whether the last index can be reached starting from the first index.
Input: int array
Output: bool

Solution:
    Track the farthest index reachable so far while traversing. If it is smaller
    than the last index after the traversal, the end cannot be reached.

    TC: O(n)
    SC: O(1)
"""


def can_end_be_reached(arr):
    farthest_index = 0
    i = 0
    while i <= farthest_index and i < len(arr):
        farthest_index = max(farthest_index, arr[i] + i)
        i += 1
    return farthest_index >= len(arr) - 1


if __name__ == "__main__":
    arr = [1, 3, 0, 0, 2, 0, 1]
    print(int(can_end_be_reached(arr)))
