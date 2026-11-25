"""River Jump: maximise the minimum jump after removing some rocks."""
import sys


def can_make_min_distance(distance, rocks, num_remove, length):
    if length < distance:
        return False
    removed = 0
    prev_rock_location = 0
    for cur_rock_location in rocks:
        if cur_rock_location - prev_rock_location < distance:
            removed += 1
        else:
            prev_rock_location = cur_rock_location
    if length - prev_rock_location < distance:
        removed += 1
    return removed <= num_remove


def solve(rocks, num_remove, length):
    low, high = 0, length + 1
    while high - low > 1:
        mid = (low + high) // 2
        if can_make_min_distance(mid, rocks, num_remove, length):
            low = mid
        else:
            high = mid
    print(low)


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    length, num_rocks, num_remove = data[0], data[1], data[2]
    rocks = sorted(data[3:3 + num_rocks])
    solve(rocks, num_remove, length)


if __name__ == "__main__":
    main()
