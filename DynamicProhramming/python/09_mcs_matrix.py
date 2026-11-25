"""Maximum sum sub-matrix using Kadane's algorithm, verified against brute force."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_ELEMENT_VALUE = 100
MAX_NUM_ROWS = 5
MAX_NUM_COLS = 5


def handle_error():
    print("Error occured ")
    sys.exit(1)


def kadane_mcs(a):
    """
    a: list of numbers for which the MCS should be found. Should have >= 1 element
    Return value: (maximum continuous sum, mcs_start_pos, mcs_end_pos)
    """
    mcs_start_pos = mcs_end_pos = 0
    cur_start_pos = 0  # store the start position of the current window
    max_local = max_global = a[0]

    # Traverse from the second element onwards
    for i in range(1, len(a)):
        max_local = max(a[i], a[i] + max_local)
        if max_local == a[i]:
            cur_start_pos = i  # start a new window here

        # Find the global maximum
        if max_local > max_global:
            max_global = max_local
            mcs_start_pos = cur_start_pos
            mcs_end_pos = i

    return max_global, mcs_start_pos, mcs_end_pos


def find_max_sum_matrix(matrix):
    """
    matrix: non-empty input matrix for which we have to find the maximum sum
    Return value: the sum of elements in the max sum sub-matrix in the input matrix
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    max_sum = float("-inf")

    for left_col in range(n_cols):
        # We have chosen a left column. The temp array stores column additions
        a = [0] * n_rows

        # Iterate through the right side columns which are >= left column
        for right_col in range(left_col, n_cols):
            # Add elements in the current right column to temp array
            for i in range(n_rows):
                a[i] += matrix[i][right_col]

            # The start and end indices returned by kadane correspond to the
            # start row and end row of the 2-D sub-matrix
            cur_sum, _start, _end = kadane_mcs(a)

            if cur_sum > max_sum:
                # The max sum sub-matrix is bounded between col1 = left_col,
                # col2 = right_col, row1 = start, row2 = end
                max_sum = cur_sum

    return max_sum


def find_brute_force_mcs(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    mcs = float("-inf")

    # Fix the start_row, end_row, start_col and end_col of the sub-matrix
    for start_row in range(n_rows):
        for end_row in range(start_row, n_rows):
            for start_col in range(n_cols):
                for end_col in range(start_col, n_cols):
                    cur_sum = sum(matrix[i][j]
                                  for i in range(start_row, end_row + 1)
                                  for j in range(start_col, end_col + 1))
                    if cur_sum > mcs:
                        mcs = cur_sum
    return mcs


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row) + " ")
    print()


def test():
    n_rows = 1 + random.randrange(MAX_NUM_ROWS)
    n_cols = 1 + random.randrange(MAX_NUM_COLS)

    # Generate random values into the matrix; some elements will be negative
    matrix = []
    for _ in range(n_rows):
        row = []
        for _ in range(n_cols):
            val = random.randrange(MAX_ELEMENT_VALUE)
            if random.randrange(2) == 0:
                val = -val
            row.append(val)
        matrix.append(row)

    print("Input : ")
    print_matrix(matrix)

    algo_mcs = find_max_sum_matrix(matrix)
    print(f"Max Continuous Sum = {algo_mcs} ")

    # The two results should match
    if algo_mcs != find_brute_force_mcs(matrix):
        handle_error()

    print("______________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
