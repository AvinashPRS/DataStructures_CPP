"""Surrounded Regions (LeetCode 130): capture 'O' regions not touching the border."""
import sys

sys.setrecursionlimit(100000)


class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        # Step 1: temporarily change every 'O' to 'P'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "P"

        # Step 2: restore regions connected to the borders
        for c in range(cols):
            self._dfs(0, c, board)
            self._dfs(rows - 1, c, board)
        for r in range(rows):
            self._dfs(r, 0, board)
            self._dfs(r, cols - 1, board)

        # Step 3: any remaining 'P' is fully surrounded
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "P":
                    board[r][c] = "X"

    def _dfs(self, row, col, board):
        rows, cols = len(board), len(board[0])
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "P":
            return
        board[row][col] = "O"  # connected to a border: restore
        self._dfs(row - 1, col, board)  # up
        self._dfs(row + 1, col, board)  # down
        self._dfs(row, col - 1, board)  # left
        self._dfs(row, col + 1, board)  # right


def print_board(board):
    for row in board:
        print("".join(f"{cell} " for cell in row))


def main():
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    print("Original board:")
    print_board(board)
    Solution().solve(board)
    print("\nBoard after solving:")
    print_board(board)


if __name__ == "__main__":
    main()
