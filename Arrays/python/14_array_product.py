"""
Compute result[i] = product of all elements of a except a[i], without division.

Solution:
    Forward pass: result[i] = product of a[0..i-1].
    Backward pass: multiply result[i] by product of a[i+1..n-1].

    TC: O(n)
    SC: O(1) besides the result
"""
import random
from math import prod

MAX_NUM_TESTS = 100
MAX_VALUE = 9
MAX_NUM_ELEMS = 9


def compute_product(a):
    n = len(a)
    result = [1] * n

    product = 1
    for i in range(n):
        result[i] = product
        product *= a[i]

    product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= product
        product *= a[i]

    return result


def verify_result(a, result):
    for i in range(len(a)):
        expected = prod(a[:i] + a[i + 1:])
        assert expected == result[i], "Test failed"


def test():
    a = [random.randint(1, MAX_VALUE) for _ in range(random.randint(1, MAX_NUM_ELEMS))]
    print("Input  :", *a)
    result = compute_product(a)
    print("Output :", *result)
    verify_result(a, result)
    print("_________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
