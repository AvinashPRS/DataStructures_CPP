"""
Given 'n', the number of steps to climb, and 'k', the max number of steps you can
take at a time, find the number of ways in which 'n' steps can be climbed.

Solution:
    For the current 'n', for each step size i <= k we can take it, after which we
    need to cover (n-i) steps.

    Base case is when n == 0, it means we have reached.
    TC: O(nk)
    SC: O(n)
"""


def ways_to_climb_stairs_tabulation(n, k):
    """
    Alternative (commented out in the original): each row i means using steps of size
    1..i. Note: this counts combinations (order doesn't matter), not ordered ways.
    """
    cache = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, k + 1):
        # zero steps can always be achieved
        cache[i][0] = 1
        for j in range(1, n + 1):
            # 'j' steps can be reached by either including current no. of steps or not
            include_step = cache[i][j - i] if i <= j else 0
            exclude_step = cache[i - 1][j] if i >= 1 else 0
            cache[i][j] = include_step + exclude_step

    return cache[-1][-1]


def ways_to_climb_stairs_memoization_helper(n, k, steps_ways):
    """finds the number of ways in which 'n' steps can be climbed using max of 'k' steps"""
    # when we have reached
    if n == 0:
        return 1
    if k <= 0:
        return 0

    if steps_ways[n] == 0:
        # for each target, find the no. of ways starting from bottom
        i = 1
        while i <= k and n - i >= 0:
            steps_ways[n] += ways_to_climb_stairs_memoization_helper(n - i, k, steps_ways)
            i += 1

    return steps_ways[n]


def ways_to_climb_stairs_memoization(n, k):
    # each entry stores the no. of ways in which that many steps can be climbed
    # steps_ways[n] = summation(steps_ways[n - i]) for all 1 <= i <= k
    steps_ways = [0] * (n + 1)

    ways = ways_to_climb_stairs_memoization_helper(n, k, steps_ways)

    print(" ".join(str(x) for x in steps_ways) + " ")
    return ways


if __name__ == "__main__":
    n = 10
    k = 3
    print(ways_to_climb_stairs_memoization(n, k))
