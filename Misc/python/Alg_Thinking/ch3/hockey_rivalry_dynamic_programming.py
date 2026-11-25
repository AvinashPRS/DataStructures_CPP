"""Hockey Rivalry - dynamic programming solution."""
import sys


def read_input():
    """Input: n, outcomes of team 1 (e.g. WLW), n goals, outcomes of team 2, n goals.
    Arrays are returned 1-indexed (index 0 unused)."""
    data = sys.stdin.read().split()
    n = int(data[0])
    pos = 1
    outcome1 = ""
    while len(outcome1) < n:
        outcome1 += data[pos]
        pos += 1
    goals1 = [int(x) for x in data[pos:pos + n]]
    pos += n
    outcome2 = ""
    while len(outcome2) < n:
        outcome2 += data[pos]
        pos += 1
    goals2 = [int(x) for x in data[pos:pos + n]]
    return n, " " + outcome1, [0] + goals1, " " + outcome2, [0] + goals2


def is_rivalry(outcome1, outcome2, goals1, goals2, i, j):
    return ((outcome1[i] == "W" and outcome2[j] == "L" and goals1[i] > goals2[j]) or
            (outcome1[i] == "L" and outcome2[j] == "W" and goals1[i] < goals2[j]))


def solve(outcome1, outcome2, goals1, goals2, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if is_rivalry(outcome1, outcome2, goals1, goals2, i, j):
                first = dp[i - 1][j - 1] + goals1[i] + goals2[j]
            else:
                first = 0
            second = dp[i - 1][j - 1]
            third = dp[i - 1][j]
            fourth = dp[i][j - 1]
            dp[i][j] = max(first, second, third, fourth)
    return dp[n][n]


def main():
    n, outcome1, goals1, outcome2, goals2 = read_input()
    print(solve(outcome1, outcome2, goals1, goals2, n))


if __name__ == "__main__":
    main()
