"""
Solve a standard 9x9 Sudoku puzzle using recursive backtracking.
Empty cells are represented by -1. Every valid solution is printed.

Rules:
- Each row, each column and each of the nine 3x3 boxes must contain the
  digits 1 through 9 with no repetition.

How the algorithm works:
- can_fill_cell: checks the row, column and 3x3 region before placing a digit.
- solve_sudoku: moves cell by cell (left to right, top to bottom). When it hits
  -1, it tries 1..9 recursively and resets the cell back to -1 (backtracking).
- verify_grid: once past the last row, prints the board and verifies that every
  row and column sums to 45.
"""
import sys

NUM_ROWS = 9
NUM_COLS = 9


def handle_error():
    print("Error occured ")
    sys.exit(1)


def verify_grid(grid):
    # The sum of the numbers in a row should be 1 + 2 + ... + 9 = 45
    for row in grid:
        if sum(row) != 45:
            handle_error()
    # The sum of the numbers in a column should be 45
    for col_nr in range(NUM_COLS):
        if sum(grid[r][col_nr] for r in range(NUM_ROWS)) != 45:
            handle_error()
    # We should also check if the sum in every 3*3 box is 45


def print_grid(grid, verify):
    for row in grid:
        print("".join(f"{v:4d} " for v in row))
    print("\n\n")
    if verify:
        verify_grid(grid)


def can_fill_cell(grid, row_nr, col_nr, num):
    """Returns True if num can be placed at (row_nr, col_nr)."""
    # Number must not be present in the column
    for i in range(NUM_ROWS):
        if grid[i][col_nr] == num:
            return False
    # Number must not be present in the row
    for j in range(NUM_COLS):
        if grid[row_nr][j] == num:
            return False
    # Number must not be present in the 3*3 box
    region_start_row = (row_nr // 3) * 3
    region_start_col = (col_nr // 3) * 3
    for i in range(region_start_row, region_start_row + 3):
        for j in range(region_start_col, region_start_col + 3):
            if grid[i][j] == num:
                return False
    return True


def solve_sudoku(grid, row_nr, col_nr):
    if row_nr >= NUM_ROWS:
        # Found a solution. Print the grid and terminate the recursion
        print_grid(grid, True)
        return

    # Pre-compute the row and column of the next cell
    next_row = row_nr
    next_col = col_nr + 1
    if next_col >= NUM_COLS:
        next_col = 0
        next_row = row_nr + 1

    if grid[row_nr][col_nr] == -1:
        # Try assigning numbers 1-9 to the cell
        for num in range(1, 10):
            if can_fill_cell(grid, row_nr, col_nr, num):
                grid[row_nr][col_nr] = num
                solve_sudoku(grid, next_row, next_col)
        # Backtracking step
        grid[row_nr][col_nr] = -1
    else:
        # The puzzle writer has already assigned a value to the cell
        solve_sudoku(grid, next_row, next_col)


def main():
    grid = [[-1] * NUM_COLS for _ in range(NUM_ROWS)]

    # Fill in the cells specified by the puzzle writer
    clues = {
        (0, 0): 5, (0, 1): 3, (0, 4): 7,
        (1, 0): 6, (1, 3): 1, (1, 4): 9, (1, 5): 5,
        (2, 1): 9, (2, 2): 8, (2, 7): 6,
        (3, 0): 8, (3, 4): 6, (3, 8): 3,
        (4, 0): 4, (4, 3): 8, (4, 5): 3, (4, 8): 1,
        (5, 0): 7, (5, 4): 2, (5, 8): 6,
        (6, 1): 6, (6, 6): 2, (6, 7): 8,
        (7, 3): 4, (7, 4): 1, (7, 5): 9, (7, 8): 5,
        (8, 4): 8, (8, 7): 7, (8, 8): 9,
    }
    for (r, c), v in clues.items():
        grid[r][c] = v

    print("Input: ")
    print_grid(grid, False)  # don't verify the input grid

    print("Output: ")
    solve_sudoku(grid, 0, 0)

    print("Test passed")


if __name__ == "__main__":
    main()
