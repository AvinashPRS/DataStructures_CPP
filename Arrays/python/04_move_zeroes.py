"""
Move all zeroes in an array to the end.

Solution:
    Two pointers: left finds the first zero from the left, right finds the first
    non-zero from the right; swap them while left < right.

    TC: O(n)
    SC: O(1)
"""
import random

MAX_NUM_TESTS = 100
MAX_NUM_ELEMS = 10
MAX_VALUE = 2


def move_zeroes(a):
    length = len(a)
    left, right = 0, length - 1

    while left < right:
        # Locate the first zero from the left
        while left < length and a[left] != 0:
            left += 1
        # Locate first non-zero from the right
        while right >= 0 and a[right] == 0:
            right -= 1
        if left < right:
            a[left], a[right] = a[right], a[left]


def verify(a):
    found_zero = False
    for value in a:
        if value == 0:
            found_zero = True
        elif found_zero:
            # Non-zero after a zero
            raise AssertionError("Test failed")


def test():
    a = [random.randrange(MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    print("Original array :", *a)
    move_zeroes(a)
    print("After moving 0 :", *a)
    verify(a)
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
