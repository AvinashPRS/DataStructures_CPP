"""Number of Islands (LeetCode 200): DFS that marks visited land as '2'."""
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
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self._dfs(row, col, grid)  # explore the whole island
        return count

    def _dfs(self, row, col, grid):
        if not self._is_valid(row, col, grid):
            return
        grid[row][col] = "2"  # mark current cell as visited
        self._dfs(row - 1, col, grid)  # up
        self._dfs(row + 1, col, grid)  # down
        self._dfs(row, col - 1, grid)  # left
        self._dfs(row, col + 1, grid)  # right

    def _is_valid(self, row, col, grid):
        if row < 0 or row >= len(grid):
            return False
        if col < 0 or col >= len(grid[0]):
            return False
        return grid[row][col] == "1"


def main():
    grid = [row[:] for row in GRID]
    print("Original Grid:")
    print_grid(grid)
    islands = Solution().numIslands(grid)
    print(f"\nNumber of Islands = {islands}")
    print("\nGrid After DFS (visited cells marked as '2'):")
    print_grid(grid)


if __name__ == "__main__":
    main()
