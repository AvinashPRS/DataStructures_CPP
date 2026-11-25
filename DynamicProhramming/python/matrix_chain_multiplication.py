"""Matrix chain multiplication: minimum number of scalar multiplications (memoized)."""
import sys

MAX = 10

# dp table to store the solution for already computed sub problems
dp = [[0] * MAX for _ in range(MAX)]


def matrix_chain_multiplication(dim, i, j):
    """Find the most efficient way to multiply the given sequence of matrices"""
    # base case: one matrix
    if j <= i + 1:
        return 0

    # if dp[i][j] is not calculated (calculate it!!)
    if dp[i][j] == 0:
        # stores minimum number of scalar multiplications (i.e., cost)
        # needed to compute the matrix M[i+1]...M[j] = M[i..j]
        min_cost = sys.maxsize

        # take the minimum over each possible position at which the
        # sequence of matrices can be split
        for k in range(i + 1, j):
            # recur for M[i+1]..M[k] to get a i x k matrix
            cost = matrix_chain_multiplication(dim, i, k)
            # recur for M[k+1]..M[j] to get a k x j matrix
            cost += matrix_chain_multiplication(dim, k, j)
            # cost to multiply two (i x k) and (k x j) matrix
            cost += dim[i] * dim[k] * dim[j]

            if cost < min_cost:
                min_cost = cost  # store the minimum cost
        dp[i][j] = min_cost

    # return min cost to multiply M[i+1]..M[j]
    return dp[i][j]


if __name__ == "__main__":
    # Matrix i has Dimensions dim[i-1] & dim[i] for i=1..n
    # input is 10 x 30 matrix, 30 x 5 matrix, 5 x 60 matrix
    dim = [10, 30, 5, 60]
    n = len(dim)
    print(f"Minimum cost is {matrix_chain_multiplication(dim, 0, n - 1)}")
