"""
N-Queens: place N queens on an NxN board so that no two queens attack each
other (same row, column or diagonal). Prints every placement as a 0/1 board.
    TC: O(n!)
"""


def display_placement(n, placement):
    for board in placement:
        for col in board:
            print("".join("1 " if j == col else "0 " for j in range(n)))
        print("\n")


def is_position_valid(col_placement):
    """Only the last queen's position is unknown; check it against the rest."""
    last_row = len(col_placement) - 1
    for i in range(last_row):
        pos_diff = abs(col_placement[i] - col_placement[last_row])
        # same column -> 0; same diagonal -> equals the row difference
        if pos_diff == 0 or pos_diff == last_row - i:
            return False
    return True


def place_n_queens(curr_row, n, col_placement, placement):
    """Backtracking over the column of the queen in curr_row."""
    if curr_row == n:
        placement.append(list(col_placement))
        return
    for i in range(n):
        col_placement.append(i)
        if is_position_valid(col_placement):
            place_n_queens(curr_row + 1, n, col_placement, placement)
        col_placement.pop()


def place_n_queens_driver(n):
    placement = []
    place_n_queens(0, n, [], placement)
    display_placement(n, placement)


if __name__ == "__main__":
    place_n_queens_driver(4)
