"""
Find the union of two arrays (result sorted, no duplicates).

Solution:
    Sort both arrays and merge them, adding an element only if it differs from
    the last element added to the result.

    TC: O(m log m + n log n)
    SC: O(m + n) for the result
"""
import random

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def find_union(a, b):
    a.sort()
    b.sort()
    result = []

    def add(x):
        if not result or result[-1] != x:
            result.append(x)

    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            add(a[i])
            if a[i] == b[j]:
                j += 1
            i += 1
        else:
            add(b[j])
            j += 1

    # Remaining elements
    for x in a[i:]:
        add(x)
    for x in b[j:]:
        add(x)

    return result


def test():
    a = [random.randrange(MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    b = [random.randrange(MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    print("A :", *a)
    print("B :", *b)

    c = find_union(a, b)
    print("Union :", *c)

    assert c == sorted(set(a) | set(b)), "Test failed"
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
