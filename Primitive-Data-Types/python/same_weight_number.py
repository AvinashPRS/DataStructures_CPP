"""
Problem:
    Weight of a number is the number of set bits in that number.
    Given a number 'x', find a number 'y' which has the same weight as 'x'
    but the absolute difference |x-y| is minimum and y != x

Input:
    x = Real number

Output:
    y = Real number
"""

# no. of bits in an unsigned int
WORD_SIZE = 32
MASK = (1 << WORD_SIZE) - 1


def same_weight_number(x):
    """
    Finds the same weight number satisfying the constraints.
    In order to have the number with same weight which is closest, we can say that
    we need to minimize 2^m - 2^n, where m>n and m and n are the indices that
    get swapped. And that difference is the difference between the original and
    new number. To minimize that we take m,n as right as possible and ensuring
    that the two are not same also. Also nth position should be adjacent to minimize.
    """
    # treat x as a 32-bit unsigned int
    x &= MASK

    for i in range(WORD_SIZE - 1):
        # if the adjacent bits are not same
        if ((x >> i) & 1) != ((x >> (i + 1)) & 1):
            # flip the bits
            x ^= (1 << i) | (1 << (i + 1))
            print(f"{i}, {i + 1}")
            return x
    # when all the bits of the number are same i.e, either 1 or 0
    return 0


if __name__ == "__main__":
    print(same_weight_number(~0))
    print(same_weight_number(6))
