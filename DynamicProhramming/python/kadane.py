"""
Given an integer list arr, find the subarray (containing at least one element) which
has the maximum possible sum, and return that sum. A subarray is a continuous part of an array.

For any element, we have two choices:
  1. Extend the maximum sum subarray ending at the previous element by adding the
     current element to it (better when that previous sum is positive).
  2. Start a new subarray at the current element (better when the previous sum is negative).
So maxEnding[i] = max(maxEnding[i-1] + arr[i], arr[i]), and the maximum of maxEnding
over all indices is the answer.
"""


def max_subarray_sum(arr):
    """Kadane's algorithm: O(n) time, O(1) space"""
    # Stores the result (maximum sum found so far)
    res = arr[0]
    # Maximum sum of subarray ending at current position
    max_ending = arr[0]

    for x in arr[1:]:
        # Either extend the previous subarray or start new from current element
        max_ending = max(x, max_ending + x)
        # Update result if the new subarray sum is larger
        res = max(res, max_ending)
    return res


def max_subarray_sum_brute_force(arr):
    """Naive approach: iterate over all subarrays - O(n^2) time and O(1) space"""
    res = arr[0]
    # Outer loop for starting point of subarray
    for i in range(len(arr)):
        curr_sum = 0
        # Inner loop for ending point of subarray
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            res = max(res, curr_sum)
    return res


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(max_subarray_sum(arr))
