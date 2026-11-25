"""
Word Break - several DP variants.
time: O(N^3) (substring takes O(N)), space: O(N)
"""


class Solution:
    def word_break(self, s, word_dict):
        """DP from the back: dp[i] is True if s[i:] can be split into dictionary words"""
        n = len(s)
        dp = [False] * (n + 1)
        # padding, assume empty string is a valid dictionary word
        dp[n] = True

        for i in range(n - 1, -1, -1):
            dp[i] = s[i:] in word_dict

            # split s[i:] into s[i:j] and s[j:], and see if the split is valid
            for j in range(n, i, -1):
                # s[j:] is composed by valid dictionary words and s[i:j] is a valid word
                dp[i] = dp[j] and s[i:j] in word_dict
                if dp[i]:
                    break

        return dp[0]


class SolutionOptimized:
    """DP optimized from above"""

    def word_break(self, s, word_dict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if dp[j] and s[i:j] in word_dict:
                    dp[i] = True
                    break

        return dp[0]


class SolutionForward:
    """DP with key: end index, 1-based"""

    def word_break(self, s, word_dict):
        n = len(s)
        dp = [False] * (n + 1)
        # empty string
        dp[0] = True

        for end in range(1, n + 1):
            for start in range(end):
                # dp[start]: s[0...start-1]
                if dp[start] and s[start:end] in word_dict:
                    # s[0...end-1] can be split into s[0...start-1] and s[start...end-1]
                    dp[end] = True
                    break

        return dp[n]


if __name__ == "__main__":
    solution = Solution()

    # Test 1
    print(int(solution.word_break("leetcode", ["leet", "code"])))

    # Test 2
    print(int(solution.word_break("applepenapple", ["apple", "pen"])))

    # Test 3
    print(int(solution.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])))
