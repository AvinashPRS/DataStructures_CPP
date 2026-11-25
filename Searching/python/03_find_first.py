"""Find the first occurrence of an element in a sorted array using binary search."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


def find_first(a, x):
    """
    a: sorted list being searched
    x: element being searched
    Returns: first position of x in a, if x is absent -1 is returned
    """
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == x:
            if mid == 0 or a[mid - 1] != x:
                return mid
            else:
                end = mid - 1
        elif a[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def find_first_brute_force(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1


def print_array(a):
    print("".join(f"{x} " for x in a))


def print_result(result, x):
    print(f"The position of first occurence of {x} is {result}")


def test_01():
    # Number of elements in the array
    n = 1 + random.randrange(MAX_NUM_ELEMS)

    a = sorted(random.randrange(MAX_VALUE) for _ in range(n))

    print("Input : ", end="")
    print_array(a)

    # Search all elements that are present and verify the result
    for x in a:
        result = find_first(a, x)
        print_result(result, x)

        expected_result = find_first_brute_force(a, x)
        if expected_result != result:
            handle_error()

    # Search for a non-existent item. Result should be -1
    x = MAX_VALUE + 1
    result = find_first(a, x)
    print_result(result, x)
    if result != -1:
        handle_error()

    print("_____________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test_01()
    print("Test passed")
