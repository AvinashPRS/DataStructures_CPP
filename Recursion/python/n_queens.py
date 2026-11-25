"""
Problem:
    Given a NxN board, the aim is to place N queens on the board such that
    no two queens can attack each other. A queen attacks another queen if the queen is in the
    same row, column or diagonal.

    TC: O(n!)

Input:
    N: dimension of board

Output:
    All possible 2D matrices depicting the placement
"""


def display_placement(n, placement):
    """Prints the position of queens on the board."""
    for col_placement in placement:
        for col in col_placement:
            print(" ".join("1" if j == col else "0" for j in range(n)) + " ")
        print("\n")


def is_position_valid(col_placement):
    """Checks whether the current queen placement is valid or not."""
    # find the total no. of row queens placed so far
    last_row = len(col_placement) - 1

    # Now all the previous queens have a valid position except for the
    # last queen, validity of whose position is not known now
    # So we check if the current column placement of queen
    # coincides with any of the columns of previous rows and diagonals
    for i in range(last_row):
        pos_diff = abs(col_placement[i] - col_placement[last_row])
        # if the column conflict is there then the pos_diff = 0
        # if the diagonal conflict is there then the pos_diff and (last_row-i) will
        # be the same, since the board is symmetric and because of which the horizontal col index diff
        # and vertical row index diff becomes the same
        if pos_diff == 0 or pos_diff == last_row - i:
            return False
    return True


def place_n_queens(curr_row, n, col_placement, placement):
    """
    For placing the N queens.
    Uses backtracking for finding the possible placement positions.
    """
    # when the current row index equals total rows that means
    # that all the queens have been placed successfully, so this placement
    # is valid
    if curr_row == n:
        # add the valid placement info
        placement.append(list(col_placement))
        return

    # try all possible column combinations
    for i in range(n):
        # try placing the queen at the current column 'i' for curr_row
        col_placement.append(i)
        # check if the position of the queen is valid or not
        if is_position_valid(col_placement):
            place_n_queens(curr_row + 1, n, col_placement, placement)
        col_placement.pop()


def place_n_queens_driver(n):
    """Driver function for N queens."""
    # for storing the placement information for all possible combinations
    placement = []
    place_n_queens(0, n, [], placement)
    display_placement(n, placement)


if __name__ == "__main__":
    place_n_queens_driver(4)
