MAX_N = 10


def check_placement(cur_row, col_for_row):
    """Return True if a queen can be placed at (cur_row, col_for_row[cur_row]).
    col_for_row[i] gives the column in which the queen of the ith row is placed."""
    # Check if the queens placed in the rows before conflict with the current one
    for i in range(cur_row):
        # Two queens in the same column
        if col_for_row[i] == col_for_row[cur_row]:
            return False
        # Two queens in the same diagonal
        if abs(col_for_row[cur_row] - col_for_row[i]) == cur_row - i:
            return False
    return True


def arrange_queens(cur_row, N, col_for_row):
    """Place queens row by row; print every successful arrangement."""
    if cur_row == N:
        # We have found a successful arrangement. So print it
        for i in range(N):
            print(f"(Row = {i}, Col = {col_for_row[i]}) ")
        print("__________________________")
        return  # Terminate the recursion

    # Try out different columns in the current row
    for i in range(N):
        col_for_row[cur_row] = i
        if check_placement(cur_row, col_for_row):
            # The placement looks good so far. Go to the next row
            arrange_queens(cur_row + 1, N, col_for_row)


# main code harness:
if __name__ == "__main__":
    col_for_rows = [0] * MAX_N
    N = 4  # Number of cells in one row of the chess board
    print(f"N = {N}")
    arrange_queens(0, N, col_for_rows)
    print("Test passed")
