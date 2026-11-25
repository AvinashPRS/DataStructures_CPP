"""
Given 'n' and 'k'. Compute the binomial coefficient.

Solution:
    The formula for (n, k) = n! / (n-k)! k!
    Computing the factorial might overflow in fixed-width ints, so use:
    (n, k) = (n-1, k) + (n-1, k-1)
    with a cache for storing the intermediate values.

    Base case will be when (k, k) or when k = 0, both are 1
    TC: O(nk)
    SC: O(nk)
"""


def find_binomial_coefficient_helper(n, k, coefficient):
    # base case
    if k == 0 or n == k:
        return 1

    # memoization step: if we have not calculated the coefficient before, compute it
    if coefficient[n][k] == 0:
        coefficient[n][k] = (find_binomial_coefficient_helper(n - 1, k, coefficient) +
                             find_binomial_coefficient_helper(n - 1, k - 1, coefficient))
    return coefficient[n][k]


def compute_binomial_coefficient(n, k):
    """finds the binomial coefficient"""
    # each (n, k) entry stores the binomial coefficient for that
    coefficient = [[0] * (k + 1) for _ in range(n + 1)]
    return find_binomial_coefficient_helper(n, k, coefficient)


if __name__ == "__main__":
    n = 5
    k = 2
    print(compute_binomial_coefficient(n, k))
