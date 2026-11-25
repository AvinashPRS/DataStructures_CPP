"""
Given a 1d list of numbers and a 2d matrix, check if the matrix contains the pattern.
We can only move left, right, up and down from a location every time.

Solution:
    Check from each location whether starting there finds the pattern. We cache the
    failed matching attempts of (i, j) for pattern[offset].

    TC: O(nms)
    SC: O(nms)
    n: no. of rows, m: no. of cols, s: pattern length
"""


def is_pattern_contained_starting_this(pattern, offset, i, j, matrix, grid_attempts):
    """checks if the pattern starting at (i, j) is contained in the matrix"""
    # if the pattern is contained fully
    if offset == len(pattern):
        return True

    # if the current location is out of grid or if this has already been tried earlier
    if (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or
            (i, j, offset) in grid_attempts):
        return False

    # if the current location matches the pattern, try all 4 directions
    if matrix[i][j] == pattern[offset]:
        if (is_pattern_contained_starting_this(pattern, offset + 1, i + 1, j, matrix, grid_attempts) or
                is_pattern_contained_starting_this(pattern, offset + 1, i - 1, j, matrix, grid_attempts) or
                is_pattern_contained_starting_this(pattern, offset + 1, i, j - 1, matrix, grid_attempts) or
                is_pattern_contained_starting_this(pattern, offset + 1, i, j + 1, matrix, grid_attempts)):
            return True  # found the pattern so return from here

    # else, add the current attempt as failed
    grid_attempts.add((i, j, offset))
    return False


def is_pattern_contained(pattern, matrix):
    """checks if a matrix contains a 1d pattern or not"""
    # contains the failed attempts for a location and the pattern offset
    grid_attempts = set()

    # we start the check from each location of matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if is_pattern_contained_starting_this(pattern, 0, i, j, matrix, grid_attempts):
                return True
    return False


if __name__ == "__main__":
    grid = [[1, 2, 3],
            [4, 3, 4],
            [7, 8, 9],
            [10, 11, 12]]
    pattern = [2, 3, 4, 7, 10]

    print(int(is_pattern_contained(pattern, grid)))
