"""
Remove duplicates from an array, in-place.

Solution:
    Sort the array, then copy an element to the fill position only when it
    differs from its predecessor.

    TC: O(n log n)
    SC: O(1) (excluding sort)
"""
import random

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def remove_duplicates(a):
    """a: non-empty list, modified in-place. Returns number of remaining elements."""
    a.sort()
    fill_pos = 1
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            a[fill_pos] = a[i]
            fill_pos += 1
    del a[fill_pos:]
    return fill_pos


def test():
    a = [random.randrange(MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    print("Original array :", *a)
    remove_duplicates(a)
    print("After removing duplicates :", *a)

    assert len(a) == len(set(a)), "Test failed"
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
