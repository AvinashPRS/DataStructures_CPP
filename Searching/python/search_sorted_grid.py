"""
Given a 2D (m X n) grid where the row and column elements are non-decreasing,
find the target element in the grid.

Input: 2D list of sorted int
Output: bool (found/not found)

Solution:
    The idea is to remove either a row or a col in every iteration. If we can do
    that then this search can be done in O(m + n - 1).
    Since rows and cols are both sorted, we can start with the smallest element of
    the largest row (bottom-left). Based on the comparison with the target we can
    remove either that row or that col from the search.

    Say we start with grid[m-1][0] and compare it with target:
    if it is larger, then all the elements in that row to the right are larger too,
    so we remove the row from the search.
    if it is smaller, then all elements above it in that col are smaller, so we
    ignore that col and make col = col + 1.

    TC: O(m + n - 1)
"""


def search_in_grid(grid, target):
    """Searches for an element in a 2D grid."""
    m = len(grid)
    n = len(grid[0]) if m else 0

    # Start with largest row and smallest column
    row = m - 1
    col = 0

    while row >= 0 and col < n:
        # If the current element is equal to the target
        if grid[row][col] == target:
            return True
        elif grid[row][col] > target:
            row -= 1
        else:
            col += 1

    return False


if __name__ == "__main__":
    grid = [[-1, 2, 4, 4, 6],
            [1, 5, 5, 9, 21],
            [7, 8, 9, 12, 25],
            [12, 13, 13, 34, 40]]

    print(int(search_in_grid(grid, 812)))
