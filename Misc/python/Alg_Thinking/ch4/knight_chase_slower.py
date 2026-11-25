"""Knight Chase - uses multiple BFS calls (one BFS would be faster)."""
import sys

KNIGHT_MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)]


def find_distance(knight_row, knight_col, dest_row, dest_col, num_rows, num_cols):
    min_moves = [[-1] * (num_cols + 2) for _ in range(num_rows + 2)]
    min_moves[knight_row][knight_col] = 0
    cur_positions = [(knight_row, knight_col)]

    while cur_positions:
        new_positions = []
        for from_row, from_col in cur_positions:
            if from_row == dest_row and from_col == dest_col:
                return min_moves[dest_row][dest_col]
            for dr, dc in KNIGHT_MOVES:
                to_row, to_col = from_row + dr, from_col + dc
                if 1 <= to_row <= num_rows and 1 <= to_col <= num_cols and \
                        min_moves[to_row][to_col] == -1:
                    min_moves[to_row][to_col] = 1 + min_moves[from_row][from_col]
                    new_positions.append((to_row, to_col))
        cur_positions = new_positions
    return -1


def solve(pawn_row, pawn_col, knight_row, knight_col, num_rows, num_cols):
    cur_pawn_row = pawn_row
    num_moves = 0
    while cur_pawn_row < num_rows:
        knight_takes = find_distance(knight_row, knight_col, cur_pawn_row,
                                     pawn_col, num_rows, num_cols)
        if knight_takes >= 0 and num_moves >= knight_takes and \
                (num_moves - knight_takes) % 2 == 0:
            print(f"Win in {num_moves} knight move(s).")
            return
        cur_pawn_row += 1
        num_moves += 1

    cur_pawn_row = pawn_row
    num_moves = 0
    while cur_pawn_row < num_rows:
        knight_takes = find_distance(knight_row, knight_col, cur_pawn_row + 1,
                                     pawn_col, num_rows, num_cols)
        if knight_takes >= 0 and num_moves >= knight_takes and \
                (num_moves - knight_takes) % 2 == 0:
            print(f"Stalemate in {num_moves} knight move(s).")
            return
        cur_pawn_row += 1
        num_moves += 1

    print(f"Loss in {num_rows - pawn_row - 1} knight move(s).")


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_cases = data[0]
    pos = 1
    for _ in range(num_cases):
        num_rows, num_cols, pawn_row, pawn_col, knight_row, knight_col = data[pos:pos + 6]
        pos += 6
        solve(pawn_row, pawn_col, knight_row, knight_col, num_rows, num_cols)


if __name__ == "__main__":
    main()
