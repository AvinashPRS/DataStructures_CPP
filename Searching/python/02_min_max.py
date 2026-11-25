"""Find the minimum and maximum in an array using ~3n/2 comparisons."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10
MAX_INT = 1000000
MIN_INT = -100000


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x} " for x in a))


def find_min_max(a):
    """
    a: input list
    Returns: (min_value, max_value)
    """
    length = len(a)
    i = 0
    max_value = MIN_INT
    min_value = MAX_INT
    if length % 2 == 1:
        # If there are odd number of elements, then initialize
        # max_value and min_value with a[0]
        max_value = min_value = a[0]
        i = 1

    while i < length:
        if a[i] > a[i + 1]:
            if a[i] > max_value:
                max_value = a[i]
            if a[i + 1] < min_value:
                min_value = a[i + 1]
        else:
            if a[i] < min_value:
                min_value = a[i]
            if a[i + 1] > max_value:
                max_value = a[i + 1]
        i += 2

    return min_value, max_value


def sorting_min_max(a):
    """
    a: input list (sorted in place)
    Returns: (min_value, max_value) found using sorting
    """
    a.sort()
    return a[0], a[-1]


def generate_array(length):
    return [random.randrange(MAX_VALUE) for _ in range(length)]


def test():
    # Randomly decide the number of elements in the array
    length = 1 + random.randrange(MAX_NUM_ELEMS)

    # Fill the array with random values
    a = generate_array(length)

    print_array(a)

    # Find the result using an efficient technique
    result_min, result_max = find_min_max(a)

    print(f"Min = {result_min}, Max = {result_max} ")

    # Find the result using sorting
    expected_min, expected_max = sorting_min_max(a)

    # The two results should match
    if result_min != expected_min or result_max != expected_max:
        handle_error()

    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
