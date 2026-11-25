"""Rope Climb: 0-1 BFS over (height, state) where state 0 = on rope,
state 1 = falling (descending is free)."""
import sys


def find_distances(target_height, jump_distance, itching):
    size = target_height * 2
    min_moves = [[-1, -1] for _ in range(size)]
    min_moves[0][0] = 0
    cur_positions = [(0, 0)]

    while cur_positions:
        new_positions = []
        i = 0
        # cur_positions can grow while we iterate (zero-cost moves)
        while i < len(cur_positions):
            from_height, from_state = cur_positions[i]
            i += 1
            if from_state == 0:
                # jump up
                to_height = from_height + jump_distance
                distance = 1 + min_moves[from_height][0]
                if to_height <= size - 1 and itching[to_height] == 0 and \
                        (min_moves[to_height][0] == -1 or
                         min_moves[to_height][0] > distance):
                    min_moves[to_height][0] = distance
                    new_positions.append((to_height, 0))
                # start falling (state 0 -> 1)
                distance = 1 + min_moves[from_height][0]
                if min_moves[from_height][1] == -1 or \
                        min_moves[from_height][1] > distance:
                    min_moves[from_height][1] = distance
                    new_positions.append((from_height, 1))
            else:
                # fall one unit down (free)
                to_height = from_height - 1
                distance = min_moves[from_height][1]
                if to_height >= 0 and (min_moves[to_height][1] == -1 or
                                       min_moves[to_height][1] > distance):
                    min_moves[to_height][1] = distance
                    cur_positions.append((to_height, 1))
                # grab the rope (state 1 -> 0, free)
                distance = min_moves[from_height][1]
                if itching[from_height] == 0 and \
                        (min_moves[from_height][0] == -1 or
                         min_moves[from_height][0] > distance):
                    min_moves[from_height][0] = distance
                    cur_positions.append((from_height, 0))
        cur_positions = new_positions
    return min_moves


def solve(target_height, min_moves):
    best = -1
    for i in range(target_height, target_height * 2):
        if min_moves[i][0] != -1 and (best == -1 or min_moves[i][0] < best):
            best = min_moves[i][0]
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
