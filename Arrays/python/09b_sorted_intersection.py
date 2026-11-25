"""
Find the intersection of two arrays (result sorted, no duplicates).

Solution:
    Sort both arrays and walk them with two pointers. When elements match, add
    it to the result if it is not a repeat.

    TC: O(m log m + n log n)
    SC: O(min(m, n)) for the result
"""
import random

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def find_intersection(a, b):
    a.sort()
    b.sort()
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            # Add only unique elements to the result
            if i == 0 or a[i] != a[i - 1]:
                result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result


def test():
    a = [random.randrange(MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    b = [random.randrange(MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    print("A :", *a)
    print("B :", *b)

    c = find_intersection(a, b)
    print("Intersection :", *c)

    assert c == sorted(set(a) & set(b)), "Test failed"
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
