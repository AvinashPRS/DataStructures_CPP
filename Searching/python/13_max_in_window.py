"""Find the maximum in every sliding window of size k using a deque."""
import sys
from collections import deque


def handle_error():
    print("Test failed")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x} " for x in a))


def compare(result, expected):
    if result != expected:
        handle_error()


def find_window_max(a, k):
    """
    a: list for which we have to find the maximum in every window of size k
    k: size of the window
    Returns: list containing the maximum in every window of size k
    """
    dq = deque()  # stores array indices
    max_values = []

    for i in range(len(a)):
        # Remove the elements outside the current window from front of deque
        while dq and dq[0] + k <= i:
            dq.popleft()

        # Remove all elements that are smaller than or equal to current
        # element from the rear of the deque
        while dq and a[i] >= a[dq[-1]]:
            dq.pop()

        # Push the index of current element into the end of the deque
        dq.append(i)

        if i >= k - 1:
            # Front of deque has index of maximum element for the current window
            max_values.append(a[dq[0]])

    return max_values


def test_01():
    a = [2, -1, 4, 3, 2, 6, 0, 7, 8, 10, 3, 2]
    expected = {
        1: [2, -1, 4, 3, 2, 6, 0, 7, 8, 10, 3, 2],
        2: [2, 4, 4, 3, 6, 6, 7, 8, 10, 10, 3],
        3: [4, 4, 4, 6, 6, 7, 8, 10, 10, 10],
    }

    print("Input                  : ", end="")
    print_array(a)

    for k in range(1, 4):
        result = find_window_max(a, k)

        print(f"Max in window of size {k}: ", end="")
        print_array(result)

        compare(result, expected[k])


if __name__ == "__main__":
    test_01()
    print("Test passed")
