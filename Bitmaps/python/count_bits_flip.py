"""
Count number of bits to be flipped to convert A to B
(https://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b/)

We are given two numbers A and B. Our task is to count the number of bits
needed to be flipped to convert A to B.

Explanation:
    A = 01010 B = 10100
    As we can see, the bits of A that need to be flipped are 01010.
    If we flip these bits, we get 10100, which is B.

Worst Case Time Complexity: O(log n)
Space complexity: O(1)
Author: Yash Raj Singh (https://github.com/yashrajyash)
"""

MASK64 = (1 << 64) - 1


def count_bits_flip(a, b):
    """
    a: the given number whose bits will be flipped to get number b
    b: the given target number
    Returns: total number of bits needed to be flipped to convert a to b
    """
    count = 0
    # restrict to 64 bits (like int64_t) so negative numbers terminate
    a = (a ^ b) & MASK64
    while a:
        a = a & (a - 1)
        count += 1
    return count


def test():
    assert count_bits_flip(10, 20) == 4
    assert count_bits_flip(20, 25) == 3
    assert count_bits_flip(7, 10) == 3
    assert count_bits_flip(17, 25) == 1
    assert count_bits_flip(11, 8) == 2
    assert count_bits_flip(21, 22) == 2
    assert count_bits_flip(7, 786) == 5
    print("All test cases successfully passed!")


if __name__ == "__main__":
    test()
