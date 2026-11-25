"""
Remove all occurrences of an element x from an array, in-place.

Solution:
    Keep a fill position; copy every element != x to the fill position.

    TC: O(n)
    SC: O(1)
"""
import random

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def remove_element(a, x):
    """Removes x from a in-place. Returns the number of remaining elements."""
    fill_pos = 0
    for value in a:
        if value != x:
            a[fill_pos] = value
            fill_pos += 1
    del a[fill_pos:]
    return fill_pos


def test():
    a = [random.randrange(MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    x = random.choice(a)

    print("Element to remove:", x)
    print("Original array :", *a)
    remove_element(a, x)
    print("After removing :", *a)

    assert x not in a, "Test failed"
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
