class Solution:
    # Helper function to perform DFS and sink the current island
    def _dfs(self, grid, r, c):
        rows, cols = len(grid), len(grid[0])

        # Base cases for recursion: boundary check and water check
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # Mark the current cell as visited by turning it into water ('0') - note this trick
        grid[r][c] = '0'

        # Recursively visit all 4 neighboring directions
        self._dfs(grid, r + 1, c)  # Down
        self._dfs(grid, r - 1, c)  # Up
        self._dfs(grid, r, c + 1)  # Right
        self._dfs(grid, r, c - 1)  # Left

    def num_islands(self, grid):
        if not grid or not grid[0]:
            return 0

        island_count = 0
        rows, cols = len(grid), len(grid[0])

        # Traverse every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                # If we encounter land ('1'), we found a new island
                if grid[r][c] == '1':
                    island_count += 1
                    # Run DFS to "sink" the entire connected island
                    self._dfs(grid, r, c)
        return island_count


if __name__ == "__main__":
    solver = Solution()
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    print("Number of islands:", solver.num_islands(grid))  # Output: 3
