"""Burger Fervor - plain recursive (slow) solution."""
import sys

sys.setrecursionlimit(100000)


def solve_t(m, n, t):
    if t == 0:
        return 0
    first = solve_t(m, n, t - m) if t >= m else -1
    second = solve_t(m, n, t - n) if t >= n else -1
    if first == -1 and second == -1:
        return -1
    return max(first, second) + 1


def solve(m, n, t):
    result = solve_t(m, n, t)
    if result >= 0:
        print(result)
    else:
        i = t - 1
        result = solve_t(m, n, i)
        while result == -1:
            i -= 1
            result = solve_t(m, n, i)
        print(f"{result} {t - i}")


def main():
    data = sys.stdin.read().split()
    for k in range(0, len(data) - 2, 3):
        solve(int(data[k]), int(data[k + 1]), int(data[k + 2]))


if __name__ == "__main__":
    main()
