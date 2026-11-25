import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def find_max(x, y):
    """Returns the maximum of x and y without using if-else and comparison"""
    difference = x - y
    # Python ints have arbitrary precision, so shifting a negative number
    # right by a large amount yields -1 (all ones); & 1 extracts the sign bit
    sign_bit = (difference >> 63) & 0x1
    # Sign bit can be 0 or 1
    # If sign bit is 0, max = x - (0 * difference) = x
    # If sign bit is 1, max = x - (1 * (x-y)) = x - x + y = y
    return x - (sign_bit * difference)


def test(x, y):
    result = find_max(x, y)

    print(f"maximum of ({x}, {y}) = {result}")

    expected_result = x if x > y else y

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test(-10, -20)
    test(-10, 20)
    test(10, -20)
    test(10, 20)
    test(0, 10)
    test(0, -20)

    print("Test passed ")
