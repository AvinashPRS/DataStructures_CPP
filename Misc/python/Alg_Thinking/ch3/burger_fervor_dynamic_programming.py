"""Burger Fervor - dynamic programming solution."""
import sys


def solve(m, n, t):
    dp = [0] * (t + 1)
    for i in range(1, t + 1):
        first = dp[i - m] if i >= m else -1
        second = dp[i - n] if i >= n else -1
        if first == -1 and second == -1:
            dp[i] = -1
        else:
            dp[i] = max(first, second) + 1

    result = dp[t]
    if result >= 0:
        print(result)
    else:
        i = t - 1
        result = dp[i]
        while result == -1:
            i -= 1
            result = dp[i]
        print(f"{result} {t - i}")


def main():
    data = sys.stdin.read().split()
    for k in range(0, len(data) - 2, 3):
        solve(int(data[k]), int(data[k + 1]), int(data[k + 2]))


if __name__ == "__main__":
    main()
