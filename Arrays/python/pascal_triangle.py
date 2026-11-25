"""
Given 'n', find the first 'n' rows of Pascal's triangle.
Input: int
Output: list of rows

Solution:
    For any row 'i', the first and last elements are 1; every element in between
    is the sum of the two elements just above it in the previous row.

    TC: O(n^2)
    SC: O(n^2)
"""


def print_pascal_triangle(triangle):
    n = len(triangle)
    for i, row in enumerate(triangle):
        print(" " * (n - i) + " ".join(map(str, row)))


def compute_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    print_pascal_triangle(compute_pascal_triangle(5))
