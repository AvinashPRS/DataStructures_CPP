"""Count inversions in an array using merge sort."""
import random
import sys

MAX_NUM_TESTS = 100
MAX_NUM_ELEMS = 10
MAX_VALUE = 10


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x} " for x in a))


def merge(a, temp, left, mid, right):
    """
    a[left..mid] and a[mid+1..right] are sorted; merge them.
    Returns the number of inversions between the two regions.
    """
    num_inversions = 0
    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
            num_inversions += mid + 1 - i
        k += 1
    # Handle any pending entries in first region
    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    # Handle any pending entries in second region
    while j <= right:
        temp[k] = a[j]
        j += 1
        k += 1
    # Restore the values from temp into a
    for i in range(left, right + 1):
        a[i] = temp[i]
    return num_inversions


def merge_sort(a, temp, left, right):
    """Sorts a[left..right] and returns the number of inversions."""
    if left >= right:
        return 0
    mid = (left + right) // 2
    num_inversions = merge_sort(a, temp, left, mid)
    num_inversions += merge_sort(a, temp, mid + 1, right)
    num_inversions += merge(a, temp, left, mid, right)
    return num_inversions


def find_inversions(a):
    temp = [0] * len(a)
    return merge_sort(a, temp, 0, len(a) - 1)


def brute_force_inversions(a):
    num_inversions = 0
    for i in range(1, len(a)):
        for j in range(i):
            if a[j] > a[i]:
                num_inversions += 1
    return num_inversions


def test():
    # Randomly decide the number of elements and fill in the array
    num_elems = 1 + random.randrange(MAX_NUM_ELEMS)
    a = [random.randrange(MAX_VALUE) for _ in range(num_elems)]
    print_array(a)

    expected_result = brute_force_inversions(a)
    result = find_inversions(a)
    print(f"Number of Inversions = {result} ")

    if result != expected_result:
        handle_error()
    print("________________________________________________")


def main():
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")


if __name__ == "__main__":
    main()
