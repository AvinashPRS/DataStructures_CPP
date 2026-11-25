"""Minimum cost path in a matrix (moves: down, right, diagonal)."""
import sys

INT_MAX = 100000


def handle_error():
    print("Error occured ")
    sys.exit(1)


def find_min_path(a):
    """
    a: non-empty 2D matrix in which we have to find the minimum cost path
    Return value: cost of the minimum path from (0, 0) to (num_rows-1, num_cols-1)
    """
    num_rows = len(a)
    num_cols = len(a[0])
    cost = [[0] * num_cols for _ in range(num_rows)]

    cost[0][0] = a[0][0]

    for i in range(1, num_rows):
        cost[i][0] = cost[i - 1][0] + a[i][0]

    for j in range(1, num_cols):
        cost[0][j] = cost[0][j - 1] + a[0][j]

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            cost[i][j] = a[i][j] + min(cost[i - 1][j], cost[i][j - 1], cost[i - 1][j - 1])

    return cost[num_rows - 1][num_cols - 1]


def min_path_r(a, cur_row, cur_col):
    if cur_row < 0 or cur_col < 0:
        return INT_MAX

    if cur_row == 0 and cur_col == 0:
        return a[0][0]

    return a[cur_row][cur_col] + min(min_path_r(a, cur_row - 1, cur_col),
                                     min_path_r(a, cur_row, cur_col - 1),
                                     min_path_r(a, cur_row - 1, cur_col - 1))


def print_matrix(m):
    for row in m:
        print("".join(f"{x:3d} " for x in row))


def test():
    a = [[5, 3, 1],
         [2, 6, 5],
         [9, 3, 1]]

    print_matrix(a)

    # Find minimum path cost using dynamic programming
    result = find_min_path(a)

    # Find minimum path cost using recursion
    expected_result = min_path_r(a, 2, 2)

    print(f"Minimum cost of path = {result}")

    # The two results should match
    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test()
    print("Test passed")
