"""Wave sort: arrange unique elements so values alternately increase and decrease."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x}, " for x in a))


def wave_sort(a):
    """
    a: list that has to be sorted so that the values in it alternatively
       increase and decrease. The elements should be unique.
    """
    # Sort the elements in ascending order
    a.sort()

    # Swap the neighboring elements
    for i in range(1, len(a) - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]


def generate_array(length):
    """Generate a list without duplicates."""
    return random.sample(range(MAX_VALUE), length)


def test():
    # Randomly pick the number of elements
    length = 1 + random.randrange(MAX_NUM_ELEMS)

    # Generate numbers in the array without any duplicates
    a = generate_array(length)

    print("Input : ", end="")
    print_array(a)

    # Perform the wave sort
    wave_sort(a)

    print("Output: ", end="")
    print_array(a)

    # Verify if the elements are alternately increasing and decreasing
    if length > 1:
        is_prev_increasing = a[0] < a[1]
        for i in range(1, length - 1):
            is_cur_increasing = a[i] < a[i + 1]
            if is_prev_increasing == is_cur_increasing:
                handle_error()
            is_prev_increasing = is_cur_increasing

    print("_________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
