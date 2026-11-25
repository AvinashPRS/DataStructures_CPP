"""
Problem: Check the parity of the bit pattern.
        Parity is 1 if the no. of set bits is odd, otherwise it is 0.

Input: Real number
Output: bool
"""


def parity1(x):
    """
    Sets parity by looking at the odd bits. We take XOR of set bits.
    XOR of odd no. of 1s is 1 and 0 for even no. of 1s.
    TC: O(n), n=no. of bits
    """
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity


def parity2(x):
    """
    Since XOR is associative as well as commutative, we can use that fact to
    divide the bit pattern into segments and subsegments. We find the XOR for the
    smallest segment and work our way up.
    TC: O(logn), n=no. of bits
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
    We traverse only the set bits.
    TC: O(k), k=no. of set bits
    """
    parity = 0
    # the loop runs for every set bit, so we are traversing
    # and counting only the set bits
    while x:
        # XOR the result with 1
        parity ^= 1
        # clear the current rightmost set bit
        x = x & (x - 1)
    return parity


if __name__ == "__main__":
    for i in range(10):
        print(f"{i}: {parity1(i)}, {parity2(i)}, {parity3(i)}")
