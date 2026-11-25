"""
Problem:
    Given a number x, index i and j. Swap the ith and jth bit in x

Input:
    x = no.
    i, j = indices

Output:
    Swapped bits representation of x

TC: O(1)
"""


def swap_bits(x, i, j):
    """
    For swapping the ith and jth bits.
    We check if the ith and jth bits are same or not.
    If the bits are same then we dont do anything
    else we flip the bits
    """
    # get the ith bit using right shift
    ith_bit = (x >> i) & 1
    # get the jth bit using right shift
    jth_bit = (x >> j) & 1

    # when the bits are not same
    if ith_bit != jth_bit:
        # mask for flipping the bits at ith and jth position
        flip_mask = (1 << i) | (1 << j)

        # XOR with 1: flips the bit
        # XOR with 0: Unchanged
        x ^= flip_mask

    return x


if __name__ == "__main__":
    print(swap_bits(5, 1, 2))
