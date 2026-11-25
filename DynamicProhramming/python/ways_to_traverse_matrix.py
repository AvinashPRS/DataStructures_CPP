"""
Find the number of ways in which you can reach the right most bottom (n-1, m-1)
location of a 2d array starting from (0, 0). We can move only right and down.

Solution:
    (n-1, m-1) can be reached only from its top or left location, and those
    locations can be reached only in a similar way.

    L(i, j) = Top + Left
    Top : L(i-1, j) when i >= 1, 0 otherwise
    Left : L(i, j-1) when j >= 1, 0 otherwise

    TC: O(nm), n: no. of rows and m: no. of columns
    SC: O(nm)

    This is the classic Unique Paths problem using recursion + memoization.
"""


def ways_to_reach_matrix_end_helper(n, m, ways_to_reach):
    """finds the no. of ways to reach (n, m) from (0, 0)"""
    # if the location has been reached
    if n == 0 and m == 0:
        return 1

    if ways_to_reach[n][m] == 0:
        # ways to reach the left location
        reach_left = 0 if m == 0 else ways_to_reach_matrix_end_helper(n, m - 1, ways_to_reach)
        # ways to reach the top location
        reach_top = 0 if n == 0 else ways_to_reach_matrix_end_helper(n - 1, m, ways_to_reach)

        ways_to_reach[n][m] = reach_left + reach_top

    return ways_to_reach[n][m]


def ways_to_reach_matrix_end(n, m):
    # each entry (i, j) stores the no. of ways that location can be reached
    ways_to_reach = [[0] * m for _ in range(n)]
    return ways_to_reach_matrix_end_helper(n - 1, m - 1, ways_to_reach)


def unique_paths(m, n):
    """Another approach: bottom-up tabulation"""
    # Create a 2D DP array initialized to 1 (first row and column have exactly 1 way)
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            # Ways to reach current cell = ways from above + ways from left
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    matrix = [[1] * 5 for _ in range(5)]
    print(f"ways to reach the desired position: {ways_to_reach_matrix_end(len(matrix), len(matrix[0]))}")
