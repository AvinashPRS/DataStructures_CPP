"""
Problem:
    Reverse the bits of a number

Input:
    x = number for reversal

Output:
    reversed number
TC: O(n), n = no. of bits
"""


def reverse_bits(x):
    """Reverses the bits (of a non-negative number)"""
    # for storing the reversed bits representation
    reversed_bits = 0

    while x:
        # left shift the number
        reversed_bits <<= 1
        # retrieve the LSB of original and make it the LSB of reversed number
        reversed_bits |= x & 1
        # right shift the original number
        x >>= 1
    return reversed_bits


if __name__ == "__main__":
    print(reverse_bits(11))
