"""Count islands of 1's in a matrix (8-directional connectivity)."""
import sys

sys.setrecursionlimit(10000)


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_matrix(m):
    for row in m:
        print("".join(f"{v} " for v in row))
    print()


def can_enter_cell(matrix, is_visited, cur_row, cur_col):
    """We shouldn't enter a cell that is out of bounds, already visited or 0."""
    n_rows, n_cols = len(matrix), len(matrix[0])
    if cur_row < 0 or cur_row >= n_rows or cur_col < 0 or cur_col >= n_cols \
            or is_visited[cur_row][cur_col] or matrix[cur_row][cur_col] == 0:
        return False
    return True


def expand_search(matrix, is_visited, cur_row, cur_col):
    """Mark the whole island containing (cur_row, cur_col) as visited."""
    is_visited[cur_row][cur_col] = True
    # Each cell has 8 neighbours
    for i in range(-1, 2):
        for j in range(-1, 2):
            if can_enter_cell(matrix, is_visited, cur_row + i, cur_col + j):
                expand_search(matrix, is_visited, cur_row + i, cur_col + j)


def find_islands(matrix):
    """Returns the number of islands of 1's in the (non-empty) matrix."""
    n_rows, n_cols = len(matrix), len(matrix[0])
    is_visited = [[False] * n_cols for _ in range(n_rows)]
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] and not is_visited[i][j]:
                # Found an island. Expand it in all directions
                expand_search(matrix, is_visited, i, j)
                count += 1
    return count


def run_test(matrix, expected_result):
    print_matrix(matrix)
    result = find_islands(matrix)
    print(f"Number of islands = {result}")
    if result != expected_result:
        handle_error()
    print("______________________________________")


def test_01():
    run_test([[1, 1, 1, 0, 0],
              [0, 1, 0, 0, 1],
              [0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0],
              [0, 1, 0, 1, 0]], 4)


def test_02():
    run_test([[1, 1, 1, 0, 0],
              [0, 1, 1, 0, 0],
              [1, 0, 1, 0, 0],
              [1, 0, 1, 0, 0],
              [0, 1, 1, 1, 0]], 1)


def main():
    test_01()
    test_02()
    print("Test passed")


if __name__ == "__main__":
    main()
