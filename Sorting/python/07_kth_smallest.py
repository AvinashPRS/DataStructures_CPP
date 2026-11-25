"""Find the kth smallest element using randomized quickselect."""
import random
import sys

MAX_NUM_TESTS = 100
MAX_NUM_ELEMS = 10
MAX_VALUE = 100
MAX_INT = 1000000


def handle_error():
    print("Test failed ")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x} " for x in a))


def partition(a, left, right):
    """
    Picks a random pivot and arranges smaller numbers to its left and greater
    numbers to its right.
    Return value: index of the pivot element of the partition
    """
    rand_pos = random.randint(left, right)

    # Pick a random element and swap it with the last element
    a[rand_pos], a[right] = a[right], a[rand_pos]

    # The last element is treated as the pivot
    pivot = a[right]

    i = left
    for j in range(left, right):
        if a[j] <= pivot:
            if i != j:
                a[i], a[j] = a[j], a[i]
            i += 1

    # Swap a[i] and the pivot that is at a[right]
    a[i], a[right] = a[right], a[i]
    return i  # The pivot is now at i


def find_kth_smallest(a, k):
    """
    a: list in which the kth smallest element should be found
    k: value of k (0 to len(a) - 1)
    Returns: the kth smallest element
    """
    left = 0
    right = len(a) - 1

    while left <= k <= right:
        pivot_pos = partition(a, left, right)
        if pivot_pos == k:
            return a[pivot_pos]
        elif pivot_pos < k:
            left = pivot_pos + 1
        else:
            right = pivot_pos - 1

    return MAX_INT  # Incorrect k value was specified


def test():
    length = 1 + random.randrange(MAX_NUM_ELEMS)
    k = random.randrange(length)

    a = [random.randrange(MAX_VALUE) for _ in range(length)]
    print_array(a)

    # Find the result using an efficient technique
    result = find_kth_smallest(a, k)
    print(f"K = {k}, Kth smallest is {result}")

    # Find the expected result using sorting
    expected_result = sorted(a)[k]

    if result != expected_result:
        handle_error()

    print("________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
