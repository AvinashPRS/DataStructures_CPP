"""Find the maximum in an array whose elements first increase and then decrease."""
import sys

MIN_INT = -999999


def handle_error():
    print("Error occured")
    sys.exit(1)


def find_max(a):
    """
    a: list where elements first increase and then decrease, len(a) > 0
    Returns: maximum element in the array
    """
    start = 0
    end = len(a) - 1
    max_element = MIN_INT

    while start <= end:
        # If only one element is left, then it is the max element
        if start == end:
            max_element = a[start]
            break

        # If two elements are left, find the maximum of the two
        if start + 1 == end:
            max_element = max(a[start], a[start + 1])
            break

        # If there are more than two elements left, then inspect the
        # middle element between start and end
        mid = (start + end) // 2

        # If middle element is greater than previous element and also
        # greater than the next element, then it is the maximum element
        if a[mid - 1] < a[mid] > a[mid + 1]:
            max_element = a[mid]
            break

        # We have not yet been able to find the max. So modify the range
        # in which the search should proceed in the next iteration
        if a[mid - 1] < a[mid] < a[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    return max_element


def print_array(a):
    print("".join(f"{x} " for x in a))


def run_test(a, expected):
    print_array(a)
    result = find_max(a)

    print(f"Maximum element = {result}")

    if result != expected:
        handle_error()

    print("_________________________________________")


if __name__ == "__main__":
    run_test([50, 40, 30, 20, 10], 50)
    run_test([30, 50, 40, 30, 20], 50)
    run_test([30, 40, 50, 20, 10], 50)
    run_test([10, 20, 30, 50, 10], 50)
    run_test([10, 20, 30, 40, 50], 50)

    print("Test passed")
