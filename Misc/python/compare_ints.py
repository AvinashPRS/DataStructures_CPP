"""Maximum of two integers without if-else or comparison (32-bit ints)."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def find_max(x, y):
    difference = x - y
    # sign bit of the 32-bit difference (Python's >> is arithmetic too)
    sign_bit = (difference >> 31) & 0x1
    # sign bit 0 -> max = x;  sign bit 1 -> max = x - (x - y) = y
    return x - (sign_bit * difference)


def test(x, y):
    result = find_max(x, y)
    print(f"maximum of ({x}, {y}) = {result}")
    if result != (x if x > y else y):
        handle_error()


def main():
    test(-10, -20)
    test(-10, 20)
    test(10, -20)
    test(10, 20)
    test(0, 10)
    test(0, -20)
    print("Test passed ")


if __name__ == "__main__":
    main()
