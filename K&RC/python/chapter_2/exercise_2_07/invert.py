"""Exercise 2-7: invert(x, p, n) returns x with the n bits that begin at
position p inverted."""

UINT_MASK = 0xFFFFFFFF  # emulate 32 bit unsigned int


def byte_to_binary(byte):
    return format(byte & 0xFF, "08b")


def invert(x, p, n):
    p += 1  # First position is 0

    mask1 = (~(~0 << n) << p) & UINT_MASK
    mask2 = ~mask1 & x

    return (mask2 | ~x) & UINT_MASK


def main():
    x = 0b11010111

    print(byte_to_binary(x))
    print(byte_to_binary(invert(x, 1, 4)))


if __name__ == "__main__":
    main()
