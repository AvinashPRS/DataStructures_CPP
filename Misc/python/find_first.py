"""Binary search for the first occurrence of x in a sorted array."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


def find_first(a, x):
    """Returns the first position of x in sorted list a, or -1."""
    start, end = 0, len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            if mid == 0 or a[mid - 1] != x:
                return mid
            end = mid - 1
        elif a[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def sort_array(a):
    """Sort in ascending order using a simple exchange sort."""
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


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
    n = 1 + random.randrange(MAX_NUM_ELEMS)
    a = [random.randrange(MAX_VALUE) for _ in range(n)]
    sort_array(a)
    print("Input : ", end="")
    print_array(a)

    # Search all elements that are present and verify the result
    for x in a:
        result = find_first(a, x)
        print_result(result, x)
        if find_first_brute_force(a, x) != result:
            handle_error()

    # Search for a non-existent item. Result should be -1
    x = MAX_VALUE + 1
    result = find_first(a, x)
    print_result(result, x)
    if result != -1:
        handle_error()
    print("_____________________________________________")


def main():
    for _ in range(MAX_NUM_TESTS):
        test_01()
    print("Test passed")


if __name__ == "__main__":
    main()
