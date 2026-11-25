"""Number of Islands using a separate visited matrix (grid is unchanged).
(The C++ file contains a duplicated, pasted-in copy of itself; this is the
single intended program.)"""
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
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += 1
                    self._dfs(row, col, grid, visited)
        return islands

    def _dfs(self, row, col, grid, visited):
        if not self._is_valid(row, col, grid, visited):
            return
        visited[row][col] = True
        self._dfs(row - 1, col, grid, visited)
        self._dfs(row + 1, col, grid, visited)
        self._dfs(row, col - 1, grid, visited)
        self._dfs(row, col + 1, grid, visited)

    def _is_valid(self, row, col, grid, visited):
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        if visited[row][col]:
            return False
        return grid[row][col] == "1"


def main():
    grid = [row[:] for row in GRID]
    print("Original Grid:")
    print_grid(grid)
    answer = Solution().numIslands(grid)
    print(f"\nNumber of Islands = {answer}")
    print("\nGrid After DFS")
    print_grid(grid)


if __name__ == "__main__":
    main()
