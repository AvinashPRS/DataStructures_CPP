"""
Find the Longest Palindromic Subsequence of a string.

A palindrome reads the same backward as forward. A subsequence can be derived from
another sequence by deleting some or no elements without changing the order of the
remaining elements.
"""


def lps(a):
    """Return the longest palindromic subsequence of string a"""
    b = a[::-1]
    m = len(a)
    res = [[0] * (m + 1) for _ in range(m + 1)]

    # Find the length of the LPS (= LCS of a and reverse(a)) bottom-up
    for i in range(m + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                res[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1])

    # Length of longest palindromic subsequence
    idx = res[m][m]
    ans = [""] * idx
    i = j = m

    # starting from right-most bottom-most corner, store chars one by one in ans
    while i > 0 and j > 0:
        # if current characters in a and b are same, it is part of the ans
        if a[i - 1] == b[j - 1]:
            ans[idx - 1] = a[i - 1]
            i -= 1
            j -= 1
            idx -= 1
        # otherwise move in the direction of the larger value
        elif res[i - 1][j] > res[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(ans)


def test():
    assert lps("radar") == "radar"
    assert lps("abbcbaa") == "abcba"
    assert lps("bbbab") == "bbbb"
    assert lps("") == ""


if __name__ == "__main__":
    test()  # execute the tests
