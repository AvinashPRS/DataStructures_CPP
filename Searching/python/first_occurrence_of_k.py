"""
Given a sorted list of elements and a target value.
Find the first occurrence of that element in the array.

Input: list of int
Output: index of first occurrence if present else -1

Solution:
    We use binary search for this. Now there are two solutions:
    1. Do binary search once and if the element is there, from there we move left
       till the current element is different than target. The last index having
       target is the answer.
       TC: O(n) + O(logn)
    2. We can prune the array. Do binary search; if the target is found, then we make
       it the first occurrence and then again search for it in the left subarray
       since if target exists before current index it will be on the left side and
       not on the right side.
       TC: O(logn)
"""


def do_find_first_occurrence(arr, target, l, h):
    """Finds the first occurrence of target element."""
    # For keeping track of first occurrence
    first_occur = -1

    while l <= h:
        # Find the middle index
        mid = l + (h - l) // 2

        if arr[mid] == target:
            # Make this the first occurrence and look for the rest
            first_occur = mid
            # Prune the right side completely
            h = mid - 1
        elif arr[mid] < target:  # when the middle element is smaller, go right
            l = mid + 1
        else:  # when the middle element is larger, go left
            h = mid - 1

    return first_occur


def find_first_occurrence(arr, target):
    """Driver function for finding the first occurrence of target element."""
    return do_find_first_occurrence(arr, target, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [-23, -1, 0, 2, 5, 6, 15, 15, 15, 123, 872, 9089]

    print(find_first_occurrence(arr, 15))
