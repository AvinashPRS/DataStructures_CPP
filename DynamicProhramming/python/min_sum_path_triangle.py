"""
Given lists of increasing size such that when placed according to their size they
form a triangle, find the min sum path value starting from the top to the bottom.

Solution:
    For finding the min path we need to know the sum of path values at each position
    in the previous level. Then we add the path values for the current level, till the
    last level. At the last level, the location with least value is the min sum path.
    TC: O(n^2)
    SC: O(n^2)
"""


def min_sum_path_triangle_value(triangle):
    """finds the min sum path value in a triangle"""
    if not triangle:
        return 0

    # stores only the immediate previous level path sums; start with pyramid top
    previous_level_sum = [triangle[0][0]]

    for i in range(1, len(triangle)):
        # the left most of current level can only be reached from the first element
        # of previous level; same goes for the right most
        curr_level_sum = [previous_level_sum[0] + triangle[i][0]]

        # from each previous location only two locations below it can be accessed
        for j in range(1, len(triangle[i]) - 1):
            curr_level_sum.append(min(previous_level_sum[j - 1] + triangle[i][j],
                                      previous_level_sum[j] + triangle[i][j]))

        curr_level_sum.append(previous_level_sum[-1] + triangle[i][-1])
        # make the current level sum the previous level sum for the upcoming level
        previous_level_sum = curr_level_sum

    # find the min in the last level
    return min(previous_level_sum)


if __name__ == "__main__":
    triangle = [[2],
                [4, 4],
                [8, 5, 6],
                [4, 2, 6, 2],
                [1, 5, 2, 3, 4]]
    print(min_sum_path_triangle_value(triangle))
