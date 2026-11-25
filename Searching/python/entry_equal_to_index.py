"""
Given a sorted array of distinct integer elements.
Find an element whose value matches its index.

Input: list of int
Output: if present return index else -1

Solution:
    We can do binary search with target element set as the middle array
    element. Then
        if the middle element equals the index
             then return
        else if middle element is greater than its index
            go left
        else if middle element is smaller than its index
            go right

    TC: O(logn)
"""


def find_element_matching_index(arr):
    """Finds an element whose value equals its index and returns its index."""
    l = 0
    h = len(arr) - 1

    while l <= h:
        # Find the middle index
        mid = l + (h - l) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:  # when the element is greater than its index
            h = mid - 1
        else:  # when the element is smaller than its index
            l = mid + 1

    return -1


if __name__ == "__main__":
    arr = [-23, -1, 0, 3, 4, 5, 15, 16, 17, 123, 872, 9089]

    print(find_element_matching_index(arr))
