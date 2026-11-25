"""
Implement a sudoku checker. The grid can be partially filled; vacant positions are
denoted by 0.
Input: 2D array
Output: bool

Solution:
    Constraints for a sudoku:
    - entries should be in [1, 9]
    - entries must be unique in each row, each column and each smaller sub-grid

    TC: O(nm), n: no. of rows and m: no. of columns
    SC: O(n)
"""
import math


def is_valid_region(grid, row_s, row_e, col_s, col_e):
    """Checks for duplicates in grid[row_s:row_e][col_s:col_e]."""
    seen = set()
    for i in range(row_s, row_e):
        for j in range(col_s, col_e):
            value = grid[i][j]
            if value != 0:
                if value in seen:
                    return False
                seen.add(value)
    return True


def is_sudoku_valid(grid):
    n = len(grid)          # no. of rows
    m = len(grid[0])       # no. of columns

    # entries should be in range
    if any(not 0 <= v <= n for row in grid for v in row):
        return False

    # row constraints
    for i in range(n):
        if not is_valid_region(grid, i, i + 1, 0, m):
            return False

    # column constraints
    for j in range(m):
        if not is_valid_region(grid, 0, n, j, j + 1):
            return False

    # sub-grid constraints
    region_size = math.isqrt(n)
    for i in range(region_size):
        for j in range(region_size):
            if not is_valid_region(grid, i * region_size, (i + 1) * region_size,
                                   j * region_size, (j + 1) * region_size):
                return False

    return True


if __name__ == "__main__":
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    print(int(is_sudoku_valid(grid)))

    # Duplicate 8 in the top-middle sub-grid -> invalid
    grid[0][3] = 8
    print(int(is_sudoku_valid(grid)))
