class Solution:
    # Helper function to perform DFS using a tracking matrix
    # note the visited is also the same dims as grid
    def _dfs(self, grid, visited, r, c):
        rows, cols = len(grid), len(grid[0])

        # Base cases: boundary check, water check, or already visited check
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or visited[r][c]:
            return

        # Mark the current cell as visited - cell visited is marked inside the island
        visited[r][c] = True

        # Recursively visit all 4 neighboring directions
        self._dfs(grid, visited, r + 1, c)  # Down
        self._dfs(grid, visited, r - 1, c)  # Up
        self._dfs(grid, visited, r, c + 1)  # Right
        self._dfs(grid, visited, r, c - 1)  # Left

    def num_islands(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        # Initialize a 2D visited grid with False values matching the dimensions
        visited = [[False] * cols for _ in range(rows)]

        # Traverse every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                # If we hit unvisited land, it's a new island
                if grid[r][c] == '1' and not visited[r][c]:
                    island_count += 1  # note where the increment is being done
                    # Run DFS to map out and mark the entire connected component
                    self._dfs(grid, visited, r, c)
        return island_count


# main code harness:
if __name__ == "__main__":
    solver = Solution()
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    print("Number of islands:", solver.num_islands(grid))  # Output: 3
