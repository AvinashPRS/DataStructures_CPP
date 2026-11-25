"""
To handle obstructions in the maze, your recursion needs an extra parameter:
a 2D grid representation where an obstruction is marked (commonly with a 1 for
a wall and 0 for an open path). You must add an explicit safety check at the very
beginning of your recursive function to instantly return 0 if the current cell is
blocked. Additionally, you can no longer use the shortcut `if i == n - 1 or j == m - 1: return 1`
because a wall might block that straight path. Instead, you check if you have successfully
reached the final cell (n-1, m-1).
"""


def count_paths_with_obstacles(i, j, n, m, grid):
    """n = total rows, m = total columns"""
    # 1. Boundary check OR if the current cell is an obstruction
    if i >= n or j >= m or grid[i][j] == 1:
        return 0

    # 2. Base case: Successfully reached the target cell (bottom-right corner)
    if i == n - 1 and j == m - 1:
        return 1

    # Move right (increases column j) + Move down (increases row i)
    right_paths = count_paths_with_obstacles(i, j + 1, n, m, grid)
    down_paths = count_paths_with_obstacles(i + 1, j, n, m, grid)

    return right_paths + down_paths


def count_paths_dp(grid):
    """Optimized approach: O(n * m) tabulation."""
    n, m = len(grid), len(grid[0])

    # If the start or end is blocked, no paths are possible
    if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
        return 0

    dp = [[0] * m for _ in range(n)]

    # Base case: Starting position
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            # Skip the starting position or any obstacle
            if (i == 0 and j == 0) or grid[i][j] == 1:
                continue

            paths_from_top = dp[i - 1][j] if i > 0 else 0
            paths_from_left = dp[i][j - 1] if j > 0 else 0

            dp[i][j] = paths_from_top + paths_from_left
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    # 0 = Empty Space, 1 = Obstruction
    grid = [
        [0, 0, 0],
        [0, 1, 0],  # Obstacle right in the middle
        [0, 0, 0],
    ]

    n = len(grid)     # Number of rows
    m = len(grid[0])  # Number of columns

    print(f"Total paths with obstacles: {count_paths_with_obstacles(0, 0, n, m, grid)}")
    # Output: 2 (Right->Right->Down->Down OR Down->Down->Right->Right)
    print(f"Total paths with obstacles (DP): {count_paths_dp(grid)}")
