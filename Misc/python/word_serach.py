"""Word Search (LeetCode 79) using DFS. O(m * n * 4^k)."""


class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y, i):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[i]:
                return False
            if i + 1 == len(word):
                return True
            c = board[x][y]
            board[x][y] = ""  # mark as used
            for dx, dy in dirs:
                if dfs(x + dx, y + dy, i + 1):
                    return True
            board[x][y] = c
            return False

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))


def main():
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    if Solution().exist(board, word):
        print("Output: true ")
    else:
        print("Output: false")


if __name__ == "__main__":
    main()
