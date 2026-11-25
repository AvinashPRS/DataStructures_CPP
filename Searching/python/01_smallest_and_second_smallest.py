"""Find the smallest and second smallest elements in an array."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10
MAX_INT = 1000000


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x} " for x in a))


def find_two_smallest(a):
    """
    a: input list
    Returns: [smallest, second smallest]
    """
    min_value = [MAX_INT, MAX_INT]

    for x in a:
        if x < min_value[0]:
            min_value[1] = min_value[0]
            min_value[0] = x
        elif x < min_value[1]:
            min_value[1] = x

    return min_value


def sorting_two_smallest(a):
    """
    a: input list (sorted in place)
    Returns: the two smallest values found using sorting
    """
    expected_result = [MAX_INT, MAX_INT]

    a.sort()

    if len(a) > 0:
        expected_result[0] = a[0]
    if len(a) > 1:
        expected_result[1] = a[1]

    return expected_result


def generate_array(length):
    return [random.randrange(MAX_VALUE) for _ in range(length)]


def test():
    # Randomly decide the number of elements in the array
    length = 1 + random.randrange(MAX_NUM_ELEMS)
    if length < 2:
        length = 2

    # Fill the array with random values
    a = generate_array(length)

    print_array(a)

    # Find the result using an efficient technique
    result = find_two_smallest(a)

    print(f"Two Smallest are = {result[0]}, {result[1]} ")

    # Find the result using sorting
    expected_result = sorting_two_smallest(a)

    # The two results should match
    if not ((result[0] == expected_result[0] and result[1] == expected_result[1])
            or (result[1] == expected_result[0] and result[0] == expected_result[1])):
        handle_error()

    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
