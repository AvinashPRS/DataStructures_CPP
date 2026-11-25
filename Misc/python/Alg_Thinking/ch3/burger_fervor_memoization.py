"""Burger Fervor - memoization solution."""
import sys

sys.setrecursionlimit(100000)


def solve_t(m, n, t, memo):
    if memo[t] != -2:
        return memo[t]
    if t == 0:
        memo[t] = 0
        return memo[t]
    first = solve_t(m, n, t - m, memo) if t >= m else -1
    second = solve_t(m, n, t - n, memo) if t >= n else -1
    if first == -1 and second == -1:
        memo[t] = -1
    else:
        memo[t] = max(first, second) + 1
    return memo[t]


def solve(m, n, t):
    memo = [-2] * (t + 1)
    result = solve_t(m, n, t, memo)
    if result >= 0:
        print(result)
    else:
        i = t - 1
        result = solve_t(m, n, i, memo)
        while result == -1:
            i -= 1
            result = solve_t(m, n, i, memo)
        print(f"{result} {t - i}")


def main():
    data = sys.stdin.read().split()
    for k in range(0, len(data) - 2, 3):
        solve(int(data[k]), int(data[k + 1]), int(data[k + 2]))


if __name__ == "__main__":
    main()
