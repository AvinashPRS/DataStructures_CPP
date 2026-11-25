"""Word Break Problem (https://leetcode.com/problems/word-break/) - top-down memoization."""


def check(s, str_set, pos, dp):
    """Checks if the string can be segmented starting from position 'pos'"""
    if pos == len(s):
        return True

    # -1 represents unvisited/uncomputed positions
    if dp[pos] != -1:
        return dp[pos] == 1

    word_till_now = ""
    for i in range(pos, len(s)):
        word_till_now += s[i]
        if word_till_now in str_set and check(s, str_set, i + 1, dp):
            dp[pos] = 1
            return True

    dp[pos] = 0
    return False


def word_break(s, word_dict):
    """Word Break solver initializer"""
    # Collect words into a set for O(1) average lookups
    str_set = set(word_dict)
    # Initialize memoization list: -1 means unvisited
    dp = [-1] * len(s)
    return check(s, str_set, 0, dp)


def test():
    s = "applepenapple"
    word_dict = ["apple", "pen"]

    assert word_break(s, word_dict)

    print(f"Test assertion output: {str(word_break(s, word_dict)).lower()}")
    print("Test implementation passed!")


if __name__ == "__main__":
    test()

    s = "applepenapple"
    word_dict = ["apple", "pen"]
    print(f"Main execution output: {int(word_break(s, word_dict))}")
