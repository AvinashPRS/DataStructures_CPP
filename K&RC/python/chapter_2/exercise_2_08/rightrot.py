"""Exercise 2-8: rightrot(x, n) returns x rotated to the right by n bits."""

UINT_BITS = 32
UINT_MASK = (1 << UINT_BITS) - 1


def printbin(x):
    print("0b" + format(x & UINT_MASK, "0%db" % UINT_BITS))


def rightrot(x, n):
    msb_1 = 1 << (UINT_BITS - 1)

    for _ in range(n):
        if x & 1:
            x = (x >> 1) | msb_1
        else:
            x = x >> 1

    return x & UINT_MASK


def main():
    x = 0b11110101

    printbin(x)
    printbin(rightrot(x, 5))


if __name__ == "__main__":
    main()

# NOTE: rightrot rotates the entire (32 bit) unsigned int, so all its bits are
# printed. Python ints are unbounded, so the width is emulated with a mask.
