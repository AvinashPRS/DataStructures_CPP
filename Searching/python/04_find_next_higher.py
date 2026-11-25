"""Find the element immediately greater than k in a sorted array."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100
MAX_INT = 999999


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x}, " for x in a))


def find_next_higher(a, k):
    """
    a: sorted list containing elements in non-decreasing order
    k: we are searching for the number immediately above k
    Returns: the number immediately greater than k in the array if it exists,
             MAX_INT otherwise
    """
    low = 0
    high = len(a) - 1

    result = MAX_INT
    while low <= high:
        mid = (low + high) // 2

        if a[mid] > k:
            result = a[mid]  # update the result and continue
            high = mid - 1
        else:
            low = mid + 1

    return result


def generate_array(length):
    return [random.randrange(MAX_VALUE) for _ in range(length)]


def test():
    # Randomly decide the number of elements
    length = 1 + random.randrange(MAX_NUM_ELEMS)

    # Generate an array having random elements and sort it
    a = generate_array(length)
    a.sort()

    print("Input : ", end="")
    print_array(a)

    # Choose a random element k in the array
    pos = random.randrange(length)
    k = a[pos]

    # Find the next higher element after k using binary search
    result = find_next_higher(a, k)

    print(f"Next element greater than {k} is {result}")

    # Find the next higher element after k using linear search
    expected_result = MAX_INT
    for i in range(pos + 1, length):
        if a[i] > k:
            expected_result = a[i]
            break

    # The linear search and binary search results should match
    if result != expected_result:
        handle_error()

    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed ")
