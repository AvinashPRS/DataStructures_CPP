"""
Check if a number is Even or Odd using Bitwise Operator
(https://www.log2base2.com/c-examples/bitwise/odd-or-even-program-in-c-using-bitwise-operator.html)

Given an integer N, determine whether it is even or odd using bitwise manipulation.
The least significant bit (LSB) of a binary number determines its parity:
- If the LSB is 0, the number is even.
- If the LSB is 1, the number is odd.

This can be checked efficiently using the bitwise AND operator (&) with 1.
- If (N & 1) == 0, N is even.
- If (N & 1) == 1, N is odd.

Example:
    Number: 10 (decimal) -> 00001010 (binary)  LSB = 0 -> Even number
    Number: 13 (decimal) -> 00001101 (binary)  LSB = 1 -> Odd number

Worst Case Time Complexity: O(1)
Space Complexity: O(1)

Author: Vedant Mukhedkar (https://github.com/git5v)
"""


def is_even(n):
    """Returns True if n is even, False if n is odd."""
    return (n & 1) == 0


def test():
    # Test Even numbers
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(100) is True
    assert is_even(-4) is True
    assert is_even(-1000) is True

    # Test Odd numbers
    assert is_even(1) is False
    assert is_even(3) is False
    assert is_even(101) is False
    assert is_even(-5) is False
    assert is_even(-999) is False

    print("All test cases successfully passed!")


if __name__ == "__main__":
    test()
