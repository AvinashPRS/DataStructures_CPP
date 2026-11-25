"""
Given two strings str1 & str2 and below operations that can be performed on str1,
find the minimum number of edits (operations) required to convert str1 into str2.
    a. Insert
    b. Remove
    c. Replace
All of the above operations are of equal cost.
"""


def edit_dist(str1, str2, m, n):
    """
    Naive recursive solution. O(3^m)
    m: length of str1, n: length of str2
    """
    if m == 0:
        return n
    if n == 0:
        return m

    # If last characters are same then continue for the rest of them.
    if str1[m - 1] == str2[n - 1]:
        return edit_dist(str1, str2, m - 1, n - 1)

    # If last not same, then 3 possibilities: Insert, Remove, Replace.
    # Get min of three and continue for rest.
    return 1 + min(edit_dist(str1, str2, m, n - 1),
                   edit_dist(str1, str2, m - 1, n),
                   edit_dist(str1, str2, m - 1, n - 1))


def edit_dist_dp(str1, str2, m, n):
    """
    DP based solution. O(m x n)
    dp[i][j] holds the minimum edits required to convert a prefix of str1 (of length i)
    into a prefix of str2 (of length j). The final answer is dp[m][n].
    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill dp in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                # If str1 empty, then add all of str2
                dp[i][j] = j
            elif j == 0:
                # If str2 empty, then remove all of str1
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                # If character same, recur for remaining
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],      # Insert
                                   dp[i - 1][j],      # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"

    print(edit_dist(str1, str2, len(str1), len(str2)))
    print(edit_dist_dp(str1, str2, len(str1), len(str2)))
