"""Rope Climb - too slow (way too many graph edges)."""
import sys


def find_distances(target_height, jump_distance, itching):
    size = target_height * 2
    min_moves = [-1] * size
    min_moves[0] = 0
    cur_positions = [0]

    def add_position(from_height, to_height, new_positions):
        if to_height <= size - 1 and itching[to_height] == 0 and \
                min_moves[to_height] == -1:
            min_moves[to_height] = 1 + min_moves[from_height]
            new_positions.append(to_height)

    while cur_positions:
        new_positions = []
        for from_height in cur_positions:
            add_position(from_height, from_height + jump_distance, new_positions)
            for j in range(from_height):
                add_position(from_height, j, new_positions)
        cur_positions = new_positions
    return min_moves


def solve(target_height, min_moves):
    best = -1
    for i in range(target_height, target_height * 2):
        if min_moves[i] != -1 and (best == -1 or min_moves[i] < best):
            best = min_moves[i]
    print(best)


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    target_height, jump_distance, num_itching = data[0], data[1], data[2]
    itching = [0] * (target_height * 2 + 1)
    for k in range(num_itching):
        start, end = data[3 + 2 * k], data[4 + 2 * k]
        for j in range(start, min(end, len(itching) - 1) + 1):
            itching[j] = 1
    min_moves = find_distances(target_height, jump_distance, itching)
    solve(target_height, min_moves)


if __name__ == "__main__":
    main()
