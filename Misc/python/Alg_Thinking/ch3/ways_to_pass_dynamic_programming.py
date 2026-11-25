"""Ways to Pass - dynamic programming solution (not in the book)."""
import sys


def solve(n, t, p):
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(t + 1):
            for m in range(p, j + 1):
                dp[i][j] += dp[i - 1][j - m]
    return dp[n][t]


def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    for i in range(k):
        n, t, p = (int(x) for x in data[1 + 3 * i:4 + 3 * i])
        print(solve(n, t, p))


if __name__ == "__main__":
    main()
