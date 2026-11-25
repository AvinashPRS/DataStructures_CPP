"""
Find the least absolute difference between any two elements of an array.

Solution:
    Sort the array; the least difference is between some pair of adjacent elements.

    TC: O(n log n)
    SC: O(1)
"""
import random

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100


def find_least_difference(a):
    assert len(a) > 1
    a.sort()
    return min(a[i + 1] - a[i] for i in range(len(a) - 1))


def brute_force_least_difference(a):
    return min(abs(a[i] - a[j]) for i in range(len(a)) for j in range(i + 1, len(a)))


def test():
    length = max(2, random.randint(1, MAX_NUM_ELEMS))
    a = [random.randrange(MAX_VALUE) for _ in range(length)]
    print(*a)

    brute_force_result = brute_force_least_difference(a)
    result = find_least_difference(a)
    print("Least difference =", result)

    assert result == brute_force_result, "Test failed"
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
