"""Merge a small sorted array into a larger sorted array that has spare room at the end."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def handle_error():
    print("Test failed")
    sys.exit(1)


def merge_arrays(a, b, m, n):
    """
    a: list of size m+n which has m elements at beginning and n spaces at end
    b: list of size n with n elements
    m: number of elements in a
    n: number of elements in b
    """
    i = m - 1
    j = n - 1
    fill_pos = m + n - 1  # Start filling from the rear of the array

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[fill_pos] = a[i]
            i -= 1
        else:
            a[fill_pos] = b[j]
            j -= 1
        fill_pos -= 1

    # Fill up the remaining elements of a if any
    while i >= 0:
        a[fill_pos] = a[i]
        i -= 1
        fill_pos -= 1

    # Fill up the remaining elements of b if any
    while j >= 0:
        a[fill_pos] = b[j]
        j -= 1
        fill_pos -= 1


def print_array(arr, num_elems):
    """Print the first num_elems values, failing if they are not sorted."""
    for i in range(num_elems):
        print(arr[i], end=" ")
        if i > 0 and arr[i - 1] > arr[i]:
            handle_error()
    print()


def sort_array(a, n):
    """Sort the first n elements in ascending order (simple exchange sort)."""
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def test_01():
    # Generate two random values m and n
    n = random.randrange(MAX_NUM_ELEMS)
    m = random.randrange(MAX_NUM_ELEMS)

    # Let a have size of (m+n) and b have a size of n
    a = [0] * (m + n)
    b = [0] * n

    for i in range(m):
        a[i] = random.randrange(MAX_VALUE)
    for i in range(n):
        b[i] = random.randrange(MAX_VALUE)

    sort_array(a, m)
    sort_array(b, n)

    print("Input1 : ", end="")
    print_array(a, m)
    print("Input2 : ", end="")
    print_array(b, n)

    merge_arrays(a, b, m, n)

    print("Output : ", end="")
    print_array(a, m + n)

    print("____________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test_01()
    print("Test passed")
