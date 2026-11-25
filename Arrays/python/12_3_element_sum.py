"""
Find all 3-element combinations in an array whose sum equals S.

Solution:
    Sort the array. For each a[i], search for the other two elements using two
    pointers starting at i+1 and the end of the array.

    TC: O(n^2)
    SC: O(1)
"""
import random

MAX_NUM_TESTS = 50
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def find_3_element_sum(a, S):
    """Returns the number of 3-element combinations that sum to S (printing each)."""
    a.sort()
    count = 0
    for i in range(len(a) - 2):
        low, high = i + 1, len(a) - 1
        while low < high:
            total = a[i] + a[low] + a[high]
            if total == S:
                count += 1
                print(f"{a[i]} + {a[low]} + {a[high]} = {total}")
                low += 1
                high -= 1
            elif total > S:
                high -= 1  # need a smaller element
            else:
                low += 1   # need a larger element
    return count


def test():
    length = random.randint(1, MAX_NUM_ELEMS)
    # Alternate elements are negative
    a = [-v if i % 2 == 0 else v
         for i, v in enumerate(random.randrange(MAX_VALUE) for _ in range(length))]
    print("Input :", *a)
    find_3_element_sum(a, 0)
    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
