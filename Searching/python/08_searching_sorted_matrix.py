"""Search an element in a matrix whose rows and columns are sorted."""
import sys


def handle_error():
    print("Error occured")
    sys.exit(1)


def search_matrix(m, x):
    """
    m: matrix to be searched (rows and columns sorted)
    x: element to search
    Returns: True if element is present, False otherwise
    """
    num_rows = len(m)
    num_cols = len(m[0]) if num_rows else 0

    i = 0
    j = num_cols - 1
    while i < num_rows and j >= 0:
        if m[i][j] == x:
            return True
        elif m[i][j] < x:
            i += 1  # go to the row below
        else:
            j -= 1  # go to the previous column

    return False


def print_matrix(m):
    for row in m:
        print("".join(f"{v:3d} " for v in row))


def print_result(result, x):
    if result:
        print(f"Found {x} ")
    else:
        print(f"Could NOT Find {x} ")


def test(m, x, expected_result):
    result = search_matrix(m, x)

    print_result(result, x)

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    m = [[10, 20, 30, 40],
         [15, 25, 35, 45],
         [27, 29, 37, 48],
         [32, 33, 39, 50]]

    print_matrix(m)

    test(m, 40, True)
    test(m, 10, True)
    test(m, 50, True)
    test(m, 25, True)
    test(m, 37, True)
    test(m, 28, False)

    print("Test passed")
