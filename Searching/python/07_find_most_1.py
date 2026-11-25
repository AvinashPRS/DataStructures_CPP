"""Find the row with the most 1's in a matrix where each row is sorted (0's then 1's)."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def find_first(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == x:
            if mid == 0 or a[mid - 1] != x:
                return mid
            else:
                end = mid - 1
        elif a[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def find_row_with_most_ones(a):
    """
    a: matrix where each row is sorted and has only 0's and 1's
    Returns: row number that has most ones, if no row has 1's then return -1
    """
    max_row = -1
    max_num_ones = 0

    for i, row in enumerate(a):
        ncols = len(row)
        # Find the position of the first 1 in the row
        first_one_index = find_first(row, 1)

        # Compute number of 1's in row based on position of the first 1
        if first_one_index == -1:
            cur_num_ones = 0  # there are no 1's in the row
        else:
            cur_num_ones = ncols - first_one_index

        if cur_num_ones > max_num_ones:
            max_num_ones = cur_num_ones
            max_row = i

    return max_row


def print_matrix(m):
    for row in m:
        print("".join(f"{v:3d} " for v in row))


def test_01():
    a = [[1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1]]

    print_matrix(a)

    result = find_row_with_most_ones(a)

    print(f"\nRow with most ones = {result}")

    if result != 0:
        handle_error()

    print("________________________________________________")


def test_02():
    a = [[0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1]]

    print_matrix(a)

    result = find_row_with_most_ones(a)

    print(f"\nRow with most ones = {result}")

    if result != 3:
        handle_error()

    print("________________________________________________")


if __name__ == "__main__":
    test_01()
    test_02()
    print("Test passed")
