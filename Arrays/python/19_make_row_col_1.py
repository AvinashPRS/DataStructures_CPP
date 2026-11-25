"""
If a cell of a matrix is 1, set all cells in its row and column to 1, using O(1)
extra space.

Solution:
    Remember whether the first row / first column originally contain a 1. Then use
    the first row and first column as markers for the rest of the matrix.

    TC: O(rows * cols)
    SC: O(1)
"""


def process_matrix(m):
    num_rows, num_cols = len(m), len(m[0])

    is_1_in_first_row = any(m[0][j] for j in range(num_cols))
    is_1_in_first_col = any(m[i][0] for i in range(num_rows))

    # Mark rows/columns that contain a 1 in the first column/row
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            if m[i][j]:
                m[i][0] = 1
                m[0][j] = 1

    # Set cells as indicated by the markers
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            if m[i][0] or m[0][j]:
                m[i][j] = 1

    if is_1_in_first_col:
        for i in range(num_rows):
            m[i][0] = 1

    if is_1_in_first_row:
        for j in range(num_cols):
            m[0][j] = 1


def print_matrix(m):
    for row in m:
        print("".join(f"{x:3d} " for x in row))
    print("\n")


if __name__ == "__main__":
    m = [[1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    expected_result = [[1, 1, 1, 1, 1],
                       [1, 0, 1, 1, 0],
                       [1, 1, 1, 1, 1],
                       [1, 0, 1, 1, 0],
                       [1, 0, 1, 1, 0]]

    print("Input: ")
    print_matrix(m)
    process_matrix(m)
    print("Output: ")
    print_matrix(m)

    assert m == expected_result, "Error occured"
    print("Test passed")
