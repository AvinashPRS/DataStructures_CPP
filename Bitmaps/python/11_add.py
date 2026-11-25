import sys

MASK32 = 0xFFFFFFFF
MAX_INT32 = 0x7FFFFFFF


def handle_error():
    print("Test failed")
    sys.exit(1)


def to_signed32(x):
    """Interpret a 32-bit pattern as a signed (two's complement) integer"""
    return x if x <= MAX_INT32 else ~(x ^ MASK32)


def add(x, y):
    """
    x, y: two integers, can be negative. x may be bigger, equal or smaller than y
    Return value: x + y
    """
    # Python ints are unbounded, so restrict the computation to 32 bits
    # to emulate C int behaviour (otherwise negative numbers loop forever)
    x &= MASK32
    y &= MASK32

    while y != 0:
        # compute the carry bits for all the bits in x and y
        carry = x & y

        # compute the sum bits for all the bits in x and y
        x = x ^ y

        # If a carry is present at current bit position, we would have
        # marked a 1 in current bit position. But the carry needs to be
        # added from the next bit position. So left shift the carry bits
        # by 1 and then add the carry in the next iteration
        y = (carry << 1) & MASK32

    return to_signed32(x)


def test(x, y):
    result = add(x, y)

    print(f"{x} + {y} = {result} ")

    # Verify the result
    if result != (x + y):
        handle_error()


if __name__ == "__main__":
    test(20, 13)
    test(20, 20)
    test(78, 100)
    test(50, -7)
    test(-8, 17)
    test(-8, -17)
    test(-25, -25)

    print("Test passed")
