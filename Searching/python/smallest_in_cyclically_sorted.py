"""
Given a cyclically sorted array of distinct integers. Find the smallest number.

Input: list of int
Output: index of the smallest number

Solution:
    We can use binary search for this. We start with left=0 and right=len-1
    then:
        while left < right:
            middle = find middle

            if middle el > right el:
                the smallest number lies in [middle+1, right]
            else (middle el < right el):
                the smallest lies in [left, middle], since all elements
                after middle are greater than middle, hence can't be smallest

        return left

    NOTE: middle el != right el since all are distinct. If duplicates are allowed
        then it takes O(n), as we can't decide where to go when middle == right.
    TC: O(logn)
"""


def find_smallest_cyclically_sorted(arr):
    """Finds the index of the smallest number in a cyclically sorted array."""
    if not arr:
        return -1

    # Lower and upper limits
    left, right = 0, len(arr) - 1

    while left < right:
        # Middle index
        middle = left + (right - left) // 2

        if arr[middle] > arr[right]:
            left = middle + 1
        else:  # right element is greater than middle element
            right = middle

    return left


if __name__ == "__main__":
    arr = [23, 314, 7888, 3, 4, 5, 15, 17, 19]

    print(find_smallest_cyclically_sorted(arr))
