import random
import sys

MAX_VALUE = 10
MAX_NUM_TESTS = 100


def handle_error():
    print("Error occured ")
    sys.exit(1)


def multiply(x, y):
    """
    x, y: two integers >= 0
    Return value: x multiplied with y
    """
    result = 0
    while y:
        # if the least significant bit of y is 1, then add x to result
        if (y & 1) == 1:
            result += x
        y = y >> 1  # shift out the least significant bit of y
        x = x << 1  # Double the value of x
    return result


def test():
    x = random.randrange(MAX_VALUE)
    y = random.randrange(MAX_VALUE)

    result = multiply(x, y)

    print(f"{x} * {y} = {result}")

    if result != x * y:
        handle_error()


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()

    print("Test passed ")
