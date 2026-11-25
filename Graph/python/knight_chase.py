"""
Knight Chase: a pawn moves one row up each turn toward the last row; find whether the knight
can capture it (win), block it (stalemate) or neither (loss). Uses BFS to compute minimum
knight moves to every square. Input format (stdin):
    num_cases
    num_rows num_cols
    pawn_row pawn_col
    knight_row knight_col
    ...
"""
import sys

KNIGHT_MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


def find_distances(knight_row, knight_col, num_rows, num_cols):
    # 1-indexed board; -1 means not reached yet
    min_moves = [[-1] * (num_cols + 1) for _ in range(num_rows + 1)]
    min_moves[knight_row][knight_col] = 0
    cur_positions = [(knight_row, knight_col)]

    while cur_positions:
        new_positions = []
        for fr, fc in cur_positions:
            for dr, dc in KNIGHT_MOVES:
                tr, tc = fr + dr, fc + dc
                if 1 <= tr <= num_rows and 1 <= tc <= num_cols and min_moves[tr][tc] == -1:
                    min_moves[tr][tc] = 1 + min_moves[fr][fc]
                    new_positions.append((tr, tc))
        cur_positions = new_positions
    return min_moves


def solve(pawn_row, pawn_col, num_rows, min_moves):
    cur_pawn_row, num_moves = pawn_row, 0
    while cur_pawn_row < num_rows:
        knight_takes = min_moves[cur_pawn_row][pawn_col]
        if knight_takes >= 0 and num_moves >= knight_takes and (num_moves - knight_takes) % 2 == 0:
            print(f"Win in {num_moves} knight move(s).")
            return
        cur_pawn_row += 1
        num_moves += 1

    cur_pawn_row, num_moves = pawn_row, 0
    while cur_pawn_row < num_rows:
        knight_takes = min_moves[cur_pawn_row + 1][pawn_col]
        if knight_takes >= 0 and num_moves >= knight_takes and (num_moves - knight_takes) % 2 == 0:
            print(f"Stalemate in {num_moves} knight move(s).")
            return
        cur_pawn_row += 1
        num_moves += 1

    print(f"Loss in {num_rows - pawn_row - 1} knight move(s).")


# main code harness:
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    num_cases, idx = data[0], 1
    for _ in range(num_cases):
        num_rows, num_cols, pawn_row, pawn_col, knight_row, knight_col = data[idx:idx + 6]
        idx += 6
        mm = find_distances(knight_row, knight_col, num_rows, num_cols)
        solve(pawn_row, pawn_col, num_rows, mm)
