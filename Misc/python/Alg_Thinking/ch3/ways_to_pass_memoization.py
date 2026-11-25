"""Ways to Pass - memoization solution."""
import sys


def solve(n, t, p, memo):
    if memo[n][t] != -1:
        return memo[n][t]
    if n == 0 and t == 0:
        return 1
    if n == 0:
        return 0
    total = 0
    for m in range(p, t + 1):
        total += solve(n - 1, t - m, p, memo)
    memo[n][t] = total
    return total


def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    for i in range(k):
        n, t, p = (int(x) for x in data[1 + 3 * i:4 + 3 * i])
        memo = [[-1] * (t + 1) for _ in range(n + 1)]
        print(solve(n, t, p, memo))


if __name__ == "__main__":
    main()
