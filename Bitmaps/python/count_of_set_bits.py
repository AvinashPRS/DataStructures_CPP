"""
Count number of set bits of a number
(https://www.geeksforgeeks.org/count-set-bits-in-an-integer/)

We are given an integer number. We need to calculate the number of set bits
in it. A binary number consists of two digits, 0 & 1. Digit 1 is known as
set bit in computer terms.

Worst Case Time Complexity: O(log n)
Space complexity: O(1)
Authors: Swastika Gupta (https://github.com/Swastyy),
         Prashant Thakur (https://github.com/prashant-th18)
"""


def count_set_bits(n):
    """
    n: non-negative number whose set bits will be counted
    Returns: total number of set bits in the binary representation of n
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    count = 0
    while n != 0:
        count += 1
        n = n & (n - 1)
    return count
    # Why this algorithm is better than the standard one?
    # Because this algorithm runs the same number of times as the number of
    # set bits in it. If the number has 3 set bits, the loop runs only 3 times.


def test():
    assert count_set_bits(4) == 1
    assert count_set_bits(6) == 2
    assert count_set_bits(13) == 3
    assert count_set_bits(9) == 2
    assert count_set_bits(15) == 4
    assert count_set_bits(25) == 3
    assert count_set_bits(97) == 3
    assert count_set_bits(31) == 5
    print("All test cases successfully passed!")


if __name__ == "__main__":
    test()
