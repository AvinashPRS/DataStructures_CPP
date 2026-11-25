"""Minimum number of jumps to reach the end of an array."""
import sys

MAX_INT = 1000000


def handle_error():
    print("Test failed ")
    sys.exit(1)


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def find_min_jumps(a):
    """
    a: a[i] contains the maximum number of locations we can jump from position i.
       Should have >= 1 element
    Return value: minimum number of jumps needed to reach the end of the array
    """
    n = len(a)
    min_jumps = [0] * n

    for i in range(1, n):
        min_jumps[i] = MAX_INT
        # Compute the minimum number of jumps to reach location i by looking
        # at the previous locations 0 to i - 1
        for j in range(i):
            if j + a[j] >= i and min_jumps[j] + 1 < min_jumps[i]:
                min_jumps[i] = min_jumps[j] + 1

    return min_jumps[n - 1]


def test():
    a = [2, 0, 2, 3, 1, 4, 2, 1, 2, 1]

    print("Input: ", end="")
    print_array(a)

    result = find_min_jumps(a)
    print(f"Minimum jumps = {result}")

    if result != 4:
        handle_error()
    print()


if __name__ == "__main__":
    test()
    print("Test passed")
