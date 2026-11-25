"""
Search in a sorted array whose length is not known (exponential search
followed by binary search). Accessing beyond the end raises IndexError,
which mirrors vector::at() throwing in the C++ version.
"""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def at(a, i):
    """Bounds-checked access (Python allows negative indices, so check explicitly)."""
    if i < 0 or i >= len(a):
        raise IndexError(i)
    return a[i]


def binary_search(a, x, low, high):
    """
    Helper function that performs binary search on an array of unknown length
    a: list which should be searched
    x: element which we are trying to find
    low: start position of region in array for searching
    high: end position of region in array for searching
    """
    while low <= high:
        mid = (low + high) // 2
        try:
            value = at(a, mid)

            if value == x:
                return mid
            elif value > x:
                high = mid - 1
            else:
                low = mid + 1
        except IndexError:
            # mid has crossed the boundary of the array. So reduce
            # the search region to (low, mid - 1)
            high = mid - 1

    return -1


def search(a, x):
    """
    Main function for performing search on array whose length is not known
    a: input list
    x: item to be searched
    Returns: if x is found, position of x is returned, otherwise -1
    """
    # Perform exponential search to first find upper bound. Start with
    # high = 0 and then increase high to 1, 2, 4, 8, 16 and so on
    low = high = 0
    while True:
        try:
            value = at(a, high)

            if value == x:
                return high  # We found the element x
            elif value > x:
                break  # We found the range (low, high) to search

            low = high + 1
            high = 1 if high == 0 else high * 2
        except IndexError:
            # We have crossed the boundary of the array. So we have
            # found the upper bound for high.
            break

    # Perform binary search in range(low, high). Note that high may still be
    # outside the array bounds
    return binary_search(a, x, low, high)


def test(length, x, expected_result):
    a = list(range(length))

    result = search(a, x)

    if length:
        print(f"Location of {x} in vector [0 to {length - 1}] is {result}")
    else:
        print(f"Location of {x} in empty vector is {result}")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test(20, 0, 0)
    test(20, 15, 15)
    test(20, 19, 19)

    test(20, 100, -1)
    test(20, -1, -1)

    test(0, 0, -1)

    print("Test passed")
