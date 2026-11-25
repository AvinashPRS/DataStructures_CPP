"""Set Matrix Zeroes: zero the whole row and column of every 0. O(m*n)."""


class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        row = [False] * m
        col = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


def print_matrix(matrix):
    for r in matrix:
        print("".join(f"{v} " for v in r))


def main():
    matrix = [[1, 2, 3],
              [4, 0, 6],
              [7, 8, 9]]
    print("Input: matrix =")
    print_matrix(matrix)
    Solution().setZeroes(matrix)
    print("\nOutput:")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
