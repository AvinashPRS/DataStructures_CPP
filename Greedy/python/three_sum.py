"""
Given a list of numbers and a sum, find whether we can get that sum by adding three numbers
from the list. A number can be repeated.

Input: list of nums, sum
Output: list of those three numbers if they exist, else an empty list

TC: O(n^2) + O(nlogn) ~ O(n^2)
"""


def has_two_sum(arr, target):
    """
    Finds two numbers whose sum equals target. arr must be sorted.
    TC: O(n)
    """
    i, j = 0, len(arr) - 1

    while i <= j:
        s = arr[i] + arr[j]
        # when the sum is found
        if s == target:
            return [arr[i], arr[j]]
        if s > target:
            j -= 1
        else:
            i += 1

    return []


def has_three_sum(arr, target):
    """Finds three numbers whose sum equals target."""
    # sort the numbers
    arr.sort()

    # for each number check if target - num is possible using two numbers
    for num in arr:
        nums = has_two_sum(arr, target - num)
        if nums:
            nums.append(num)
            return nums
    return []


if __name__ == "__main__":
    arr = [12, 11, 2, 3, 7, 1, 10]
    target = 8
    print(" ".join(str(x) for x in has_three_sum(arr, target)))
