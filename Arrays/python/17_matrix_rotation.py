"""
Rotate a square matrix by 90 degrees clockwise, in-place.

Solution 1: four-way swap of the cells in the first quadrant.
Solution 2: transpose the matrix, then reverse each row.

    TC: O(n^2)
    SC: O(1)
"""


def rotate_square_matrix_90(m):
    n = len(m)
    # max_i and max_j are the boundaries of the first quadrant
    max_i = (n // 2) - 1
    max_j = ((n + 1) // 2) - 1
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            # Four way swap
            temp = m[i][j]
            m[i][j] = m[n - j - 1][i]
            m[n - j - 1][i] = m[n - i - 1][n - j - 1]
            m[n - i - 1][n - j - 1] = m[j][n - i - 1]
            m[j][n - i - 1] = temp


def swap_rows(m):
    """Flips the matrix vertically (first row <-> last row, ...)."""
    n = len(m)
    for i in range(n // 2):
        m[i], m[n - 1 - i] = m[n - 1 - i], m[i]


def swap_columns(m):
    """Flips the matrix horizontally (first column <-> last column, ...)."""
    n = len(m)
    for row in m:
        for j in range(n // 2):
            row[j], row[n - 1 - j] = row[n - 1 - j], row[j]


def matrix_transpose(m):
    n = len(m)
    for i in range(n):
        for j in range(i):
            m[i][j], m[j][i] = m[j][i], m[i][j]


def print_matrix(m):
    for row in m:
        print("".join(f"{x:3d} " for x in row))


def make_matrix(n):
    return [[i * n + j + 1 for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    m = make_matrix(5)
    rotate_square_matrix_90(m)
    print_matrix(m)

    # Verify against transpose + horizontal flip
    m2 = make_matrix(5)
    matrix_transpose(m2)
    swap_columns(m2)
    assert m == m2, "Error occured"

    print("Test passed")
