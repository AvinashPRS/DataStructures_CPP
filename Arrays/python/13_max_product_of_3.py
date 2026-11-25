"""
Find the maximum product of any 3 elements in an array.

Solution:
    In one pass track the 3 largest and the 2 smallest values. The answer is
    max(max1*max2*max3, min1*min2*max1) (two negatives may produce a large product).

    TC: O(n)
    SC: O(1)
"""
import random
from itertools import combinations

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def find_max_product(a):
    assert len(a) >= 3
    max_value = [float("-inf")] * 3
    min_value = [float("inf")] * 2

    for x in a:
        # Check if x is among the 3 largest values
        if x > max_value[0]:
            max_value = [x, max_value[0], max_value[1]]
        elif x > max_value[1]:
            max_value = [max_value[0], x, max_value[1]]
        elif x > max_value[2]:
            max_value[2] = x

        # Check if x is among the 2 smallest values
        if x < min_value[0]:
            min_value = [x, min_value[0]]
        elif x < min_value[1]:
            min_value[1] = x

    return max(max_value[0] * max_value[1] * max_value[2],
               min_value[0] * min_value[1] * max_value[0])


def brute_force_max_product(a):
    return max(x * y * z for x, y, z in combinations(a, 3))


def test():
    length = max(3, random.randrange(MAX_NUM_ELEMS))
    a = [random.randrange(MAX_VALUE) * random.choice((1, -1)) for _ in range(length)]
    print(*a)

    result = find_max_product(a)
    print("Max product =", result)

    assert result == brute_force_max_product(a), "Test failed"
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
