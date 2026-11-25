"""
Find the non repeating integer in an array of repeating integers.
Single Number (https://leetcode.com/problems/single-number/)

Given an array of integers in which all of the numbers occur exactly
twice except one integer which occurs only once. Find the non-repeating
integer.

Worst Case Time Complexity: O(n)
Space complexity: O(1)
Author: Ravidev Pandey (https://github.com/literalEval)
"""


def find_non_repeating_integer(nums):
    """
    nums: list of integers
    Returns: the integer that occurs only once
    """
    # The idea is based on the property of XOR.
    # We know that 'a' XOR 'a' is '0' and '0' XOR 'b' is b.
    # Using this, if we XOR all the elements of the array,
    # the repeating elements will give '0' and this '0'
    # with the single number will give the number itself.
    xor = 0
    for num in nums:
        xor ^= num
    return xor


def test():
    assert find_non_repeating_integer([1, 1, 2, 2, 4, 5, 5]) == 4
    assert find_non_repeating_integer([203, 3434, 4545, 3434, 4545]) == 203
    assert find_non_repeating_integer([90, 1, 3, 90, 3]) == 1
    print("All test cases successfully passed!")


if __name__ == "__main__":
    test()
