"""Exercise 2-9: faster bitcount using x &= (x - 1)."""

UINT_BITS = 32


def printbits(x):
    print("0b" + format(x, "0%db" % UINT_BITS))


def bitcount(x):
    b = 0
    while x:
        x &= x - 1
        b += 1
    return b


def main():
    x = 0b011010

    printbits(x)
    print("x have %d bits of 1." % bitcount(x))


if __name__ == "__main__":
    main()

# NOTE: The expression x &= (x - 1) deletes the rightmost 1-bit of x.
