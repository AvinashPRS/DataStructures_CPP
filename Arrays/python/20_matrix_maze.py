"""
Count the number of paths from the bottom-right cell to the top-left cell of a maze,
moving up, left or diagonally up-left. Cells with -1 cannot be traversed.

Solution:
    Recursively try the three moves from the current cell.

    TC: O(3^(rows + cols))
    SC: O(rows + cols) recursion depth
"""
from functools import lru_cache

NOT_ALLOWED = -1


def navigate_maze(m, cur_row, cur_col):
    """Returns the number of paths from (cur_row, cur_col) to (0, 0)."""
    if cur_row < 0 or cur_col < 0:
        return 0
    if m[cur_row][cur_col] == NOT_ALLOWED:
        return 0
    if cur_row == 0 and cur_col == 0:
        return 1

    return (navigate_maze(m, cur_row - 1, cur_col)          # previous row
            + navigate_maze(m, cur_row, cur_col - 1)        # previous column
            + navigate_maze(m, cur_row - 1, cur_col - 1))   # diagonal


@lru_cache(maxsize=None)
def golden_number_of_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return (golden_number_of_paths(m - 1, n) + golden_number_of_paths(m, n - 1)
            + golden_number_of_paths(m - 1, n - 1))


def print_matrix(m):
    for row in m:
        print("".join(f"{x:3d} " for x in row))
    print("\n")


if __name__ == "__main__":
    rows, cols = 5, 5
    m = [[0] * cols for _ in range(rows)]

    print("Input: ")
    print_matrix(m)

    num_paths = navigate_maze(m, rows - 1, cols - 1)
    print("Number of paths =", num_paths)

    golden_num_paths = golden_number_of_paths(rows, cols)
    print("Golden number of paths =", golden_num_paths)

    assert num_paths == golden_num_paths, "Error occured"
    print("Test passed")
