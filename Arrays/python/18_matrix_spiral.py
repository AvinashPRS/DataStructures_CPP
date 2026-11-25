"""
Print a matrix in spiral order.

Solution:
    Maintain boundaries r1, r2 (rows) and c1, c2 (columns). Print the top row,
    right column, bottom row and left column, shrinking the boundaries after each.

    TC: O(rows * cols)
    SC: O(1)
"""


def spiral_order(m):
    result = []
    r1, r2 = 0, len(m) - 1
    c1, c2 = 0, len(m[0]) - 1 if m else -1

    while r1 <= r2 and c1 <= c2:
        # Row r1
        for col in range(c1, c2 + 1):
            result.append(m[r1][col])
        r1 += 1

        # Column c2
        for row in range(r1, r2 + 1):
            result.append(m[row][c2])
        c2 -= 1

        if r1 <= r2:
            # Row r2
            for col in range(c2, c1 - 1, -1):
                result.append(m[r2][col])
            r2 -= 1

        if c1 <= c2:
            # Column c1
            for row in range(r2, r1 - 1, -1):
                result.append(m[row][c1])
            c1 += 1

    return result


def print_spiral(m):
    print(*spiral_order(m))


if __name__ == "__main__":
    m = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
    print_spiral(m)
    assert spiral_order(m) == [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6,
                               7, 8, 9, 14, 19, 18, 17, 12, 13]
    # Non-square matrices
    assert spiral_order([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    print("Test passed")
