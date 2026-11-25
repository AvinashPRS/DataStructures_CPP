"""Binary Search (recursive and iterative)."""


def do_binary_search(arr, value_to_search, l, h):
    """Recursive binary search. Returns the index if found else -1."""
    if l > h:
        return -1

    # Find the middle index
    mid = l + (h - l) // 2

    if arr[mid] == value_to_search:
        return mid
    elif arr[mid] > value_to_search:
        return do_binary_search(arr, value_to_search, l, mid - 1)
    else:
        return do_binary_search(arr, value_to_search, mid + 1, h)


def do_binary_search_iter(arr, value_to_search, l, h):
    """Iterative binary search. Returns the index if found else -1."""
    while l <= h:
        # Find the middle index
        mid = l + (h - l) // 2

        # Check the left, right and middle conditions
        if arr[mid] == value_to_search:
            return mid
        elif arr[mid] > value_to_search:
            h = mid - 1
        else:
            l = mid + 1

    # When the element is not found
    return -1


def binary_search(arr, value_to_search):
    """Driver function for doing binary search."""
    l = 0  # lower index
    h = len(arr) - 1  # upper index

    # return do_binary_search(arr, value_to_search, l, h)
    return do_binary_search_iter(arr, value_to_search, l, h)


if __name__ == "__main__":
    arr = [-23, -1, 0, 2, 5, 6, 123, 872, 9089]

    print(binary_search(arr, 6))
