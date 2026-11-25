"""Least number of dice throws to finish a snake and ladder board."""
import sys

MAX_POSITIONS_ON_BOARD = 100


def handle_error():
    print("Error occured ")
    sys.exit(1)


def find_least_throws(is_snake, ladder, predecessor):
    """
    is_snake: if there is a snake at position 20, then is_snake[20] is True
    ladder: if there is a ladder from position 30 to 44, then ladder[44] = 30.
        if there is no ladder at location 90 then ladder[90] = -1
    predecessor: filled with the previous board position from where we came to
        current position with least number of dice throws.
    Return value: least number of throws to reach the final position on the board
    """
    # least_throws[pos] = least number of dice throws required to reach pos
    least_throws = [0] * (MAX_POSITIONS_ON_BOARD + 1)

    # Positions from 1 to 6 can be reached from a single dice throw
    for pos in range(1, 7):
        least_throws[pos] = 1
        predecessor[pos] = 0

    for pos in range(7, MAX_POSITIONS_ON_BOARD + 1):
        min_throws = MAX_POSITIONS_ON_BOARD

        # Find how many dice throws are needed to reach pos from any of the 6 previous cells
        for i in range(1, 7):
            prev_pos = pos - i
            if is_snake[prev_pos]:
                continue
            # Pick the minimum throws needed from the 6 previous cells
            if least_throws[prev_pos] + 1 < min_throws:
                min_throws = least_throws[prev_pos] + 1
                predecessor[pos] = prev_pos

        # If ladder[14] = 4, there is a ladder from 4 to 14, so throws needed to
        # reach 14 = throws needed to reach 4
        ladder_start_pos = ladder[pos]
        if ladder_start_pos != -1:
            if least_throws[ladder_start_pos] < min_throws:
                min_throws = least_throws[ladder_start_pos]
                predecessor[pos] = ladder_start_pos

        least_throws[pos] = min_throws

    return least_throws[MAX_POSITIONS_ON_BOARD]


def main():
    is_snake = [False] * (MAX_POSITIONS_ON_BOARD + 1)
    ladder = [-1] * (MAX_POSITIONS_ON_BOARD + 1)
    predecessor = [0] * (MAX_POSITIONS_ON_BOARD + 1)

    for pos in (17, 54, 62, 64, 87, 93, 95, 99):
        is_snake[pos] = True

    ladders = {14: 4, 31: 9, 38: 20, 84: 28, 59: 40, 67: 51, 81: 63, 91: 71}
    for end, start in ladders.items():
        ladder[end] = start

    min_throws = find_least_throws(is_snake, ladder, predecessor)
    print(f"Least number of throws = {min_throws}")

    if min_throws != 7:
        handle_error()

    print("The positions on the board corresponding to dice throws in reverse order are: ")
    i = MAX_POSITIONS_ON_BOARD
    print(i)
    while i > 0:
        print(predecessor[i])
        i = predecessor[i]

    print("Test passed")


if __name__ == "__main__":
    main()
