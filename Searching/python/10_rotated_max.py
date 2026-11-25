"""Find the maximum element in a sorted and rotated array (no duplicates)."""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_NUM_TESTS = 10


def handle_error():
    print("Error occured")
    sys.exit(1)


def find_max(a):
    """
    a: list that has been sorted and rotated. There should NOT be any duplicates
    Returns: maximum element in the array
    """
    n = len(a)
    assert n > 0
    start = 0
    end = n - 1

    while a[start] > a[end]:
        mid = (start + end) // 2

        if mid < n - 1 and a[mid] > a[mid + 1]:
            return a[mid]

        if a[mid] > a[end]:
            start = mid  # max is in the region (mid, end)
        else:
            end = mid - 1  # max is in the region (start, mid - 1)

    return a[end]


def print_array(a):
    print("".join(f"{x} " for x in a))


def generate_sorted_rotated_array(n):
    # Generate the first random value
    a = [random.randrange(10)]

    # Generate the remaining random values in increasing sorted order without duplication
    for _ in range(1, n):
        a.append(a[-1] + 1 + random.randrange(10))

    # Randomly decide the number of rotations and perform them
    num_rotations = random.randrange(n)
    if num_rotations:
        a = a[-num_rotations:] + a[:-num_rotations]

    return a


def test_01():
    # Randomly decide the number of elements
    n = 1 + random.randrange(MAX_NUM_ELEMENTS)

    # Generate the sorted rotated array
    a = generate_sorted_rotated_array(n)

    print("Input : ", end="")
    print_array(a)

    # Find the max using linear search
    test_result = max(a)

    # Find the max using binary search
    actual_result = find_max(a)

    print(f"The maximum element is {actual_result}")

    # Compare the results of linear and binary search
    if test_result != actual_result:
        handle_error()

    print("_______________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test_01()
    print("Test passed ")
