"""Rotate an n x n matrix 90 degrees clockwise in place. O(n^2)."""


def rotate(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row to rotate clockwise
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]


def print_matrix(matrix):
    for row in matrix:
        print("".join(f"{v} " for v in row))


def main():
    # Case 1: [[1,2,3],[4,5,6],[7,8,9]]
    # Case 2:
    matrix = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]
    print("Input: matrix = ")
    print_matrix(matrix)
    rotate(matrix)
    print("\nOutput:")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
