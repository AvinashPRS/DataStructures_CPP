"""
Given an array of int, find the length of the longest subset such that for any two elements in it,
all the numbers between them are also in it. They need not appear sequentially in the original
array. eg: 1,2,8,3 -> <1,2,3>

Input: array of int
Output: int

Solution:
    Use a hash set to keep track of numbers not yet assigned to an interval.
    Initially the set is filled with all distinct numbers.
    Pick one number from the set and expand in the +1 and -1 directions.
    Numbers found are removed from the set so they aren't processed again.

    TC: O(n)
    SC: O(m), m: no. of distinct numbers
"""


def longest_contained_interval(arr):
    avail_nums = set(arr)
    longest_interval = 0

    while avail_nums:
        num = avail_nums.pop()

        # find all numbers smaller than it
        lower = num - 1
        while lower in avail_nums:
            avail_nums.remove(lower)
            lower -= 1

        # find all numbers greater than it
        upper = num + 1
        while upper in avail_nums:
            avail_nums.remove(upper)
            upper += 1

        longest_interval = max(longest_interval, upper - lower - 1)

    return longest_interval


if __name__ == "__main__":
    arr = [10, 5, 3, 11, 6, 100, 4]
    print(longest_contained_interval(arr))
