"""
Given an unsorted array of distinct elements, find the Kth largest element.
K is 1 indexed.
Input: list of int
Output: int

Solution:
    We can randomly select a pivot element, then find its pivot position.
    Now:
        if the pivot index is K-1: then done
        else if pivot index > k-1:
            upper limit = pivot_index - 1
        else if pivot index < k-1:
            lower_limit = pivot_index + 1

    TC: O(n) avg case   [T(n) = T(n/2) + O(n)]
        O(n^2) worst case
"""
import operator
import random
import sys


def place_pivot_element(arr, pivot_index, left, right, compare):
    """Places the pivot element at its correct position."""
    pivot_value = arr[pivot_index]
    # For keeping track of last index of larger elements till now
    curr_big = left

    # Swap the pivot with last element
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    # We use two pointers for arranging the elements.
    # For finding the kth largest element, we will first have all elements
    # greater than the pivot then all elements smaller than the pivot
    for i in range(left, right):
        # We do swapping only when the current element is greater than pivot
        if compare(arr[i], pivot_value):
            arr[i], arr[curr_big] = arr[curr_big], arr[i]
            curr_big += 1

    # Swap the pivot to its correct position
    arr[curr_big], arr[right] = arr[right], arr[curr_big]

    return curr_big


def find_kth_largest_element(arr, k, compare=operator.gt):
    """Finds the kth largest element."""
    # When the array size is lesser than k
    if len(arr) < k:
        return -sys.maxsize - 1

    left, right = 0, len(arr) - 1

    while left <= right:
        # Generate random index for pivot
        pivot_index = random.randint(left, right)

        # Find the pivot partition position
        partition_pos = place_pivot_element(arr, pivot_index, left, right, compare)

        if partition_pos == k - 1:
            return arr[partition_pos]
        elif partition_pos > k - 1:
            right = partition_pos - 1
        else:
            left = partition_pos + 1

    return None


if __name__ == "__main__":
    k = 4
    arr = [2, 23, -23, -442, 99, 10, 34, 998, 634, -872]

    print(f"{k}th largest: {find_kth_largest_element(arr, k, operator.gt)}")

    arr.sort(reverse=True)
    # Verify the result using sorted array
    print(" ".join(str(a) for a in arr) + " ")
    print(f"Using sorting: {arr[k - 1]}")
