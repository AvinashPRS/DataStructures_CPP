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
    """Reverses the bits (only the significant bits, no leading zeros)"""
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


def reverse_number(num):
    """Reverses the decimal digits of num - this is not related to bits"""
    reversed_num = 0
    while num:
        reversed_num *= 10
        # add the last digit
        reversed_num += num % 10
        # remove the last digit from the original num
        num //= 10
    return reversed_num


def swap_bits(x, i, j):
    # get the ith and jth bits using right shift
    ith_bit = (x >> i) & 1
    jth_bit = (x >> j) & 1

    # when the bits are not same
    if ith_bit != jth_bit:
        # mask for flipping the bits at ith and jth position
        flip_mask = (1 << i) | (1 << j)
        # XOR with 1: flips the bit, XOR with 0: unchanged
        x ^= flip_mask

    return x


def count_set_bits(x):
    """TC: O(n), n = no. of bits in number representation"""
    set_bits = 0
    # traverse through the bits
    while x:
        set_bits += x & 1
        x >>= 1
    return set_bits


def count_set_bits2(x):
    """
    TC: O(s), s = no. of set bits
    We can efficiently count the set bits by going through only the set bits.
    Using the x & (x-1) expression we can clear the rightmost set bit.
    """
    set_bits = 0
    while x:
        set_bits += 1
        x &= x - 1  # clears the rightmost set bit
    return set_bits


def parity1(x):
    """
    Computes parity by looking at every bit. We take XOR of the bits:
    XOR of odd no. of 1s is 1 and 0 for even no. of 1s.
    TC: O(n), n = no. of bits
    """
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity


def parity2(x):
    """
    Since XOR is associative as well as commutative, we can use that fact to
    divide the bit pattern into segments and subsegments. We find the XOR for
    the smallest segment and work our way up.
    TC: O(log n), n = no. of bits
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    # retrieve the final parity bit
    return x & 0x1


def parity3(x):
    """
    We traverse only the set bits
    TC: O(k), k = no. of set bits
    """
    parity = 0
    while x:
        # XOR the result with 1
        parity ^= 1
        # clear the current rightmost set bit
        x &= x - 1
    return parity


if __name__ == "__main__":
    print("reversed bit representation in decimal would be:", reverse_bits(11))
    print(reverse_number(123))

    print(swap_bits(5, 1, 2))

    print(f"{count_set_bits(0)}, {count_set_bits2(0)}")
    print(f"{count_set_bits(1)}, {count_set_bits2(1)}")
    print(f"{count_set_bits(7)}, {count_set_bits2(7)}")

    # check the parity code:
    for i in range(10):
        print(f"{i}: {parity1(i)}, {parity2(i)}, {parity3(i)}")

    print("===========SUCCESS==========")
