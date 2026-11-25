"""Search for a sequence (pattern) in a 2D grid, moving to an adjacent cell
(up/down/left/right) for each next entry. Memoises failed (x, y, offset)
attempts. (EPI 16.4 "Search for a sequence in a 2D array")

Usage: string_in_matric.py [n]
"""
import random
import sys


def rand_matrix(n):
    return [[random.randint(0, n - 1) for _ in range(n)] for _ in range(n)]


def is_pattern_contained_in_grid(grid, pattern):
    # Each entry is a point in the grid and a suffix of the pattern (its
    # offset). Presence means the suffix is NOT contained starting there.
    previous_attempts = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_pattern_suffix_contained_starting_at_xy(
                    grid, i, j, pattern, 0, previous_attempts):
                return True
    return False


def is_pattern_suffix_contained_starting_at_xy(grid, x, y, pattern, offset,
                                               previous_attempts):
    if len(pattern) == offset:
        return True  # nothing left to complete
    # (x, y) outside the grid, or already known to fail
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) or \
            (x, y, offset) in previous_attempts:
        return False
    if grid[x][y] == pattern[offset] and any(
            is_pattern_suffix_contained_starting_at_xy(
                grid, nx, ny, pattern, offset + 1, previous_attempts)
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))):
        return True
    previous_attempts.add((x, y, offset))
    return False


def main(argv):
    sys.setrecursionlimit(10000)
    n = int(argv[1]) if len(argv) == 2 else random.randint(2, 10)
    a = rand_matrix(n)
    for row in a:
        print("".join(f"{v} " for v in row))
    s = [random.randint(0, n - 1) for _ in range(1 + random.randint(1, n * n // 2))]
    print("S = " + "".join(f"{v} " for v in s))
    print(str(is_pattern_contained_in_grid(a, s)).lower())


if __name__ == "__main__":
    main(sys.argv)
