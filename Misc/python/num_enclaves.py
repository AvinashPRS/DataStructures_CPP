"""Number of Enclaves (LeetCode 1020): land cells that can't reach the border."""
import sys

sys.setrecursionlimit(100000)


class Solution:
    def numEnclaves(self, grid):
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        # Remove land connected to left and right boundaries
        for row in range(rows):
            self._dfs(row, 0, grid)
            self._dfs(row, cols - 1, grid)
        # Remove land connected to top and bottom boundaries
        for col in range(cols):
            self._dfs(0, col, grid)
            self._dfs(rows - 1, col, grid)
        return sum(cell == 1 for row in grid for cell in row)

    def _dfs(self, row, col, grid):
        rows, cols = len(grid), len(grid[0])
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
            return
        grid[row][col] = 0
        self._dfs(row - 1, col, grid)
        self._dfs(row + 1, col, grid)
        self._dfs(row, col - 1, grid)
        self._dfs(row, col + 1, grid)


def main():
    grid = [[0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
    print(f"Number of enclave land cells: {Solution().numEnclaves(grid)}")


if __name__ == "__main__":
    main()
