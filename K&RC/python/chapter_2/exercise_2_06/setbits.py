"""Exercise 2-6: setbits(x, p, n, y) returns x with the n bits that begin at
position p set to the rightmost n bits of y."""

UINT_MASK = 0xFFFFFFFF  # emulate 32 bit unsigned int


def byte_to_binary(byte):
    return format(byte & 0xFF, "08b")


def setbits(x, p, n, y):
    p += 1  # First position is 0

    mask1 = (~(~(~0 << n) << p) & x) & UINT_MASK
    mask2 = ((~(~0 << n) & y) << p) & UINT_MASK

    return mask1 | mask2


def main():
    x = 0b11111111
    y = 0b0110

    print(byte_to_binary(x))
    print(byte_to_binary(setbits(x, 2, 4, y)))


if __name__ == "__main__":
    main()

# NOTE: Masking is a very good technique to work with bits. We can think about
# logic AND as a multiply and for OR as an addition.
