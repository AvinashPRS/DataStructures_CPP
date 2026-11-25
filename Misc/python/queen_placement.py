"""N-Queens: print every arrangement of N non-attacking queens
(same program as 02_n_queen)."""

MAX_N = 10


def check_placement(cur_row, col_for_row):
    """
    Checks if it is possible to place the queen of cur_row at
    column col_for_row[cur_row].
    col_for_row[i] gives the column in which queen of the ith row is placed.
    Returns True if the queen can be placed, False otherwise.
    """
    for i in range(cur_row):
        # Two queens in the same column
        if col_for_row[i] == col_for_row[cur_row]:
            return False
        # Two queens in the same diagonal
        col_diff = abs(col_for_row[cur_row] - col_for_row[i])
        row_diff = cur_row - i
        if row_diff == col_diff:
            return False
    return True


def arrange_queens(cur_row, n, col_for_row):
    """
    cur_row: current row in which the queen should be placed
    n: the number of cells in 1 row of the chess board
    col_for_row: col_for_row[i] stores the column of the ith row queen
    """
    if cur_row == n:
        # We have found a successful arrangement, so print it
        for i in range(n):
            print(f"(Row = {i}, Col = {col_for_row[i]}) ")
        print("__________________________")
        return

    # Try out different columns in the current row
    for i in range(n):
        col_for_row[cur_row] = i
        if check_placement(cur_row, col_for_row):
            # Placement looks good so far. Go to the next row
            arrange_queens(cur_row + 1, n, col_for_row)


def main():
    col_for_rows = [0] * MAX_N
    n = 4  # Number of cells in one row of the chess board
    print(f"N = {n}")
    arrange_queens(0, n, col_for_rows)
    print("Test passed")


if __name__ == "__main__":
    main()
