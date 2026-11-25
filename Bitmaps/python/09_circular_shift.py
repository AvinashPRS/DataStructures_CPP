import sys

SIZE = 32  # number of bits in unsigned int
MASK32 = 0xFFFFFFFF


def handle_error():
    print("Error occured ")
    sys.exit(1)


def circular_left_shift(value, n):
    """
    value: input value which has to be circularly shifted left
    n: number of positions to shift
    Return value: result after circularly left shifting value
    """
    n = n % SIZE
    return ((value << n) | (value >> (SIZE - n))) & MASK32


def circular_right_shift(value, n):
    """
    value: input value which has to be circularly shifted right
    n: number of positions to shift
    Return value: result after circularly right shifting value
    """
    n = n % SIZE
    return ((value >> n) | (value << (SIZE - n))) & MASK32


if __name__ == "__main__":
    if circular_right_shift(0x1, 1) != 0x80000000:
        handle_error()

    if circular_right_shift(0xFEDCBA98, 32) != 0xFEDCBA98:
        handle_error()

    if circular_right_shift(0xFEDCBA98, 16) != 0xBA98FEDC:
        handle_error()

    if circular_left_shift(0x1, 0x80000000) != 1:
        handle_error()

    if circular_left_shift(0xFEDCBA98, 32) != 0xFEDCBA98:
        handle_error()

    if circular_left_shift(0xFEDCBA98, 16) != 0xBA98FEDC:
        handle_error()

    print("Test passed ")
