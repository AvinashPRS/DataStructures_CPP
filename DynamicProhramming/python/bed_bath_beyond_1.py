"""Word break: check whether a string can be segmented into dictionary words."""


def word_break(s, dictionary):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    # Traverse through the given string
    for i in range(1, n + 1):
        # Traverse through the dictionary words
        for w in dictionary:
            # Check if current word is present and the prefix before the word
            # is also breakable
            start = i - len(w)
            if start >= 0 and dp[start] and s[start:i] == w:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    s = "ilike"
    dictionary = ["i", "like", "gfg"]
    print("true" if word_break(s, dictionary) else "false")
