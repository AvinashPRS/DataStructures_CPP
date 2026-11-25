"""
Pascal's triangle element lookup using top-down recursion + memoization.
"""


class PascalMemo:
    def __init__(self, max_rows):
        # Initialize DP table with -1 to represent uncomputed states
        self.memo = [[-1] * max_rows for _ in range(max_rows)]

    def get_element(self, row, col):
        """Returns the value at (row, col) using top-down recursion + memoization."""
        # Base cases: first/last column or top of the triangle
        if col == 0 or col == row:
            return 1

        # Return cached result if already computed
        if self.memo[row][col] != -1:
            return self.memo[row][col]

        # Recursive relation: C(r, c) = C(r-1, c-1) + C(r-1, c)
        self.memo[row][col] = self.get_element(row - 1, col - 1) + self.get_element(row - 1, col)
        return self.memo[row][col]


if __name__ == "__main__":
    pt = PascalMemo(35)
    print(f"Row 5, Col 2: {pt.get_element(5, 2)}")  # Output: 10
    print(f"Row 6, Col 3: {pt.get_element(6, 3)}")  # Output: 20
