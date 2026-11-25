"""Subtract two integers using only bitwise operators (32-bit two's complement)."""
import sys

MASK = 0xFFFFFFFF


def handle_error():
    print("Test failed")
    sys.exit(1)


def to_signed32(x):
    x &= MASK
    return x - (1 << 32) if x & 0x80000000 else x


def subtract(x, y):
    """x, y: two integers, can be negative. Returns x - y."""
    x &= MASK
    y &= MASK
    while y != 0:
        # borrow bits for all the bit positions
        borrow = (~x) & y & MASK
        # difference bits for all the bit positions
        x = x ^ y
        # the borrow must be subtracted from the next bit position
        y = (borrow << 1) & MASK
    return to_signed32(x)


def test(x, y):
    result = subtract(x, y)
    print(f"{x} - {y} = {result} ")
    if result != x - y:
        handle_error()


def main():
    test(20, 13)
    test(20, 20)
    test(78, 100)
    test(50, -7)
    test(-8, 17)
    test(-8, -17)
    test(-25, -25)
    print("Test passed")


if __name__ == "__main__":
    main()
