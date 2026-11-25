"""
Print the values of a 2D matrix in spiral form.
Input: 2D array
Output: elements in spiral order

Solution:
    Track the start/end row and column. Print the top, right, bottom and left sides,
    shrinking the bounds after each.

    TC: O(nm), n: no. of rows and m: no. of columns
    SC: O(1)
"""


def spiral(grid):
    result = []
    if not grid:
        return result
    row_s, row_e = 0, len(grid) - 1
    col_s, col_e = 0, len(grid[0]) - 1

    while row_s <= row_e and col_s <= col_e:
        # top side
        for i in range(col_s, col_e + 1):
            result.append(grid[row_s][i])
        row_s += 1

        # right side
        for i in range(row_s, row_e + 1):
            result.append(grid[i][col_e])
        col_e -= 1

        # bottom side (only if a row is left)
        if row_s <= row_e:
            for i in range(col_e, col_s - 1, -1):
                result.append(grid[row_e][i])
            row_e -= 1

        # left side (only if a column is left)
        if col_s <= col_e:
            for i in range(row_e, row_s - 1, -1):
                result.append(grid[i][col_s])
            col_s += 1

    return result


def print_spiral(grid):
    print(*spiral(grid))


if __name__ == "__main__":
    matrix = [[1, 2, 3, 33],
              [4, 5, 6, 66],
              [7, 8, 9, 99],
              [10, 11, 12, 122]]
    print_spiral(matrix)
    print_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
