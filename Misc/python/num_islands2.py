"""Number of Islands using a nested (closure) DFS function."""
import sys

sys.setrecursionlimit(100000)

GRID = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]


def print_grid(grid):
    for row in grid:
        print("".join(f"{c} " for c in row))


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or \
                    grid[row][col] != "1" or visited[row][col]:
                return
            visited[row][col] = True
            dfs(row - 1, col)  # up
            dfs(row + 1, col)  # down
            dfs(row, col - 1)  # left
            dfs(row, col + 1)  # right

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += 1
                    dfs(row, col)
        return islands


def main():
    grid = [row[:] for row in GRID]
    print("Original Grid:")
    print_grid(grid)
    print(f"\nNumber of Islands = {Solution().numIslands(grid)}")


if __name__ == "__main__":
    main()
