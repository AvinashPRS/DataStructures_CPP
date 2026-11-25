"""
Replace every element of an array with the greatest element to its right.
The last element is replaced with -1.

Solution:
    Process the array from the back, keeping track of the greatest value seen so far.

    TC: O(n)
    SC: O(1)
"""
import random

MAX_NUM_ITEMS = 10
MAX_VALUE = 100
INVALID_NUMBER = -1


def replace_with_next_greatest(a):
    """a: list (len >= 1), modified in-place."""
    n = len(a)
    next_greatest = a[n - 1]
    a[n - 1] = INVALID_NUMBER

    # Process the array from backwards
    for i in range(n - 2, -1, -1):
        temp = a[i]
        a[i] = next_greatest
        if temp > next_greatest:
            next_greatest = temp


def brute_force(b):
    n = len(b)
    result = list(b)
    for i in range(n - 1):
        result[i] = max(b[i + 1:])
    result[n - 1] = INVALID_NUMBER
    return result


def test_01():
    n = random.randint(1, MAX_NUM_ITEMS)
    a = [random.randrange(MAX_VALUE) for _ in range(n)]
    expected = brute_force(a)

    print("Input:", *a)
    replace_with_next_greatest(a)
    print("Output:", *a)

    assert a == expected, "Test failed"


if __name__ == "__main__":
    for _ in range(10):
        test_01()
        print("\n__________________________________\n")
    print("Test passed")
