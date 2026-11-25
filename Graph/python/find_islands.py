"""Count islands of 1's in a 0/1 matrix, where cells are connected in all 8 directions."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_matrix(m):
    for row in m:
        print(" ".join(str(x) for x in row) + " ")
    print()


def can_enter_cell(matrix, is_visited, r, c):
    """We shouldn't enter if out of bounds, already visited, or the cell value is 0."""
    n_rows, n_cols = len(matrix), len(matrix[0])
    return 0 <= r < n_rows and 0 <= c < n_cols and not is_visited[r][c] and matrix[r][c] != 0


def expand_search(matrix, is_visited, r, c):
    """Mark the whole island containing (r, c). Each cell has 8 neighbours."""
    is_visited[r][c] = True
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if can_enter_cell(matrix, is_visited, r + i, c + j):
                expand_search(matrix, is_visited, r + i, c + j)


def find_islands(matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])
    is_visited = [[False] * n_cols for _ in range(n_rows)]  # Initially nothing visited
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] and not is_visited[i][j]:
                # We have found an island. Now expand the island in all directions
                expand_search(matrix, is_visited, i, j)
                count += 1
    return count


def run_test(matrix, expected):
    print_matrix(matrix)
    result = find_islands(matrix)
    print(f"Number of islands = {result}")
    if result != expected:
        handle_error()
    print("______________________________________")


def test_01():
    run_test([
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
    ], 4)


def test_02():
    run_test([
        [1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
    ], 1)


# main code harness:
if __name__ == "__main__":
    test_01()
    test_02()
    print("Test passed")
