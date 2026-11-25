"""
Problem: Count the number of set bits in binary representation of a number

Input: Real number

Output: No. of set bits
"""


def count_set_bits(x):
    """
    For counting no. of set bits.
    TC: O(n), n=no. of bits in number representation
    """
    set_bits = 0
    # traverse through the bits
    while x:
        set_bits += x & 1
        x >>= 1
    return set_bits


def count_set_bits2(x):
    """
    Counts set bits.
    TC: O(s), s=no. of set bits
    We can efficiently count the set bits by going through only the set bits.
    Using the x & (x-1) expression we can clear the rightmost set bit.
    """
    set_bits = 0
    while x:
        set_bits += 1
        # clear the rightmost bit
        x = x & (x - 1)
    return set_bits


if __name__ == "__main__":
    print(f"{count_set_bits(0)}, {count_set_bits2(0)}")
    print(f"{count_set_bits(1)}, {count_set_bits2(1)}")
    print(f"{count_set_bits(7)}, {count_set_bits2(7)}")
