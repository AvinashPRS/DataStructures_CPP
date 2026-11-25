"""
Count the paths from the top-left to the bottom-right of an n x m grid, moving only right or down.

While recursion works perfectly for small grids, it calculates the exact same subproblems repeatedly.
For a larger grid (like 10 x 10), this code will run incredibly slow because its time complexity is
exponential: O(2^(n+m)).
"""


def count_paths(i, j, n, m):
    """n = total rows, m = total columns"""
    # Out of bounds boundary check
    if i >= n or j >= m:
        return 0

    # Shortcut: If you reach the last row or last column,
    # there is only 1 straight path left to the destination.
    if i == n - 1 or j == m - 1:
        return 1

    # Move right (increases column j) + Move down (increases row i)
    return count_paths(i, j + 1, n, m) + count_paths(i + 1, j, n, m)


def count_paths_dp(n, m):
    """
    Dynamic Programming (Tabulation) - O(n * m) Time

    Math Formula (Combinatorics) - O(n) Time, O(1) Space:
    Because you must always take exactly (n-1) down moves and (m-1) right moves, this is a
    permutation problem. The answer is simply the combination ((n-1)+(m-1)) choose (n-1).
    """
    dp = [[0] * m for _ in range(n)]

    # Fill the grid
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1  # Base edges only have 1 path
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    n, m = 5, 5
    print(f"Total paths: {count_paths(0, 0, n, m)}")  # Output: 70
    print(f"Total paths (DP): {count_paths_dp(n, m)}")
