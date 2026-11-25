"""
Examples of memoization with recursion: 1D list, 2D list and dict caches.
"""


def fib(n, memo):
    """
    A naive recursive Fibonacci takes O(2^n) time because it recalculates the same subproblems
    repeatedly. Storing results in a list reduces the time complexity to O(n).
    """
    # Base cases
    if n <= 1:
        return n

    # 1. Check if the result is already cached
    if memo[n] != -1:
        return memo[n]

    # 2. Compute, store in cache, and return
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def count_paths(r, c, rows, cols, memo):
    """
    When a recursive function depends on two changing parameters - such as (row, col)
    coordinates on a grid - use a 2D list to cache the state. This drops the runtime from
    exponential to O(rows x cols).

    Count paths from (r, c) to bottom-right corner moving only Right or Down.
    """
    # Out of bounds
    if r >= rows or c >= cols:
        return 0

    # Reached destination
    if r == rows - 1 and c == cols - 1:
        return 1

    # Return cached value if already computed
    # Not visited - already initialized to -1
    if memo[r][c] != -1:
        return memo[r][c]

    # Cache sum of moving down and moving right
    memo[r][c] = count_paths(r + 1, c, rows, cols, memo) + count_paths(r, c + 1, rows, cols, memo)
    return memo[r][c]


def can_construct(target, word_bank, memo):
    """Example: Recursive Word Break check with string memoization."""
    if not target:
        return True

    # 1. Look up the current target string in the dict
    if target in memo:
        return memo[target]

    for word in word_bank:
        # Check if target starts with 'word'
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


if __name__ == "__main__":
    n = 45
    # Initialize cache with -1 (meaning "uncomputed")
    memo = [-1] * (n + 1)
    print(f"Fib({n}) = {fib(n, memo)}")

    rows, cols = 15, 15
    memo2 = [[-1] * cols for _ in range(rows)]
    print(f"Unique paths: {count_paths(0, 0, rows, cols, memo2)}")

    memo1 = {}
    words = ["e", "ee", "eee", "eeee", "eeeee"]
    target = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"  # Worst-case backtracking trap
    print(f"Can construct: {str(can_construct(target, words, memo1)).lower()}")
