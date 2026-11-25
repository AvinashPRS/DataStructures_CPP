"""
Rotate an array to the right by num_rotations positions, in-place.

Solution:
    Reverse the whole array, then reverse the first k elements and the remaining
    n - k elements separately (k = num_rotations % n).

    TC: O(n)
    SC: O(1)
"""


def reverse_array(a, low, high):
    """Reverses a[low..high] in-place."""
    while low < high:
        a[low], a[high] = a[high], a[low]
        low += 1
        high -= 1


def rotate_array(a, num_rotations):
    length = len(a)
    # Rotating by length gives the same array
    num_rotations %= length
    if num_rotations == 0:
        return

    reverse_array(a, 0, length - 1)
    reverse_array(a, 0, num_rotations - 1)
    reverse_array(a, num_rotations, length - 1)


def perform_test(a, num_rotations, expected_result):
    print("Num Rotations =", num_rotations)
    print("Before Rotating:", *a)
    rotate_array(a, num_rotations)
    assert a == expected_result, "Error occured"
    print("After  Rotating:", *a)
    print("________________________________________")


if __name__ == "__main__":
    perform_test([10], 1, [10])
    perform_test([10, 20, 30, 40, 50], 1, [50, 10, 20, 30, 40])
    perform_test([10, 20, 30, 40, 50], 2, [40, 50, 10, 20, 30])
    perform_test([10, 20, 30, 40, 50], 4, [20, 30, 40, 50, 10])
    perform_test([10, 20, 30, 40, 50], 5, [10, 20, 30, 40, 50])
    print("Test passed")
