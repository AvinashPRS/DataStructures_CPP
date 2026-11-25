"""Search an element in a sorted and rotated array (no duplicates) with one binary search."""
import random
import sys

MAX_NUM_ELEMENTS = 10
MAX_NUM_ITERATIONS = 100


def handle_error():
    print("Error occured")
    sys.exit(1)


def find_element(a, x):
    """
    a: list that has been sorted and rotated. There should not be any duplicates
    x: element to be searched in the array
    Returns: location of the element in array if found, -1 if not found
    """
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if x == a[mid]:
            return mid

        # Check which portion of the array has elements in sorted order
        if a[start] <= a[mid]:
            # The lower portion (start, mid) is still sorted even after
            # rotations. So use this portion for taking decisions
            if a[start] <= x < a[mid]:
                end = mid - 1  # search in region (start, mid-1)
            else:
                start = mid + 1  # search in region (mid+1, end)
        else:
            # The upper portion (mid, end) is sorted even after
            # rotations. So use this portion for taking decisions
            if a[mid] < x <= a[end]:
                start = mid + 1  # search in region (mid+1, end)
            else:
                end = mid - 1  # search in region (start, mid-1)

    return -1


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

    for index, x in enumerate(a):
        # Search the element using binary search
        actual_result = find_element(a, x)

        print(f"Location of {x} is {actual_result}")

        # Verify the result
        if actual_result != index:
            handle_error()

    print("_________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_ITERATIONS):
        test_01()
    print("Test passed ")
