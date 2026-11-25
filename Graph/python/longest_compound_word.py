import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_words(words):
    for w in words:
        print(w)


def word_break(str1, dictionary):
    """True if str1 can be broken into 2 or more words from the dictionary."""
    length = len(str1)
    if length == 0:
        return False

    # if we can break the string from 0 to pos, then is_break_possible[pos] is True
    is_break_possible = [False] * length
    # if the substring from i to j is a word in dictionary, then word_start[j] is i
    word_start = [-1] * length

    for i in range(length):
        # Check if the substring from 0 to i is in the dictionary
        if not is_break_possible[i] and str1[:i + 1] in dictionary:
            is_break_possible[i] = True
            word_start[i] = 0

        # If we can break the substring up to i into dictionary words, then check if
        # substrings starting from i+1 can be broken into dictionary words
        if is_break_possible[i]:
            for j in range(i + 1, length):
                if not is_break_possible[j] and str1[i + 1:j + 1] in dictionary:
                    # We can form a word from i+1 to j
                    is_break_possible[j] = True
                    word_start[j] = i + 1

    # word_start[length-1] == 0 means the whole word is itself in the dictionary;
    # we want a compound word made of 2 or more dictionary words.
    return is_break_possible[length - 1] and word_start[length - 1] != 0


def find_longest_compound_word(words):
    """Returns the longest compound word, or None."""
    dictionary = set(words)
    # Sort the words so that the longest word appears first
    words.sort(key=len, reverse=True)
    for w in words:
        if word_break(w, dictionary):
            return w
    return None  # There is no compound word in the input


def test_01():
    words = ["hello", "jack", "lumber", "hellolumberjack", "hellojack"]
    print_words(words)
    longest = find_longest_compound_word(words)
    if longest:
        print("Longest compound word =", longest)
    if longest != "hellolumberjack":
        handle_error()
    print("________________________________________")


def test_02():
    words = ["hello", "jack", "lumber"]
    print_words(words)
    longest = find_longest_compound_word(words)
    if longest:
        print("Longest compound word =", longest)
    else:
        print("No compound word possible ")
    if longest is not None:
        handle_error()
    print("________________________________________")


# --- Alternative, simpler DP version (was commented out in the C++ file) ---
def is_compound_word(word, d):
    n = len(word)
    if n == 0:
        return False
    # dp[i] is True if the prefix word[0..i-1] can be formed by dictionary words
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if j == 0 and i == n:
                continue  # Skip checking the entire word against itself
            if dp[j] and word[j:i] in d:
                dp[i] = True
                break
    return dp[n]


# main code harness:
if __name__ == "__main__":
    test_01()
    test_02()
    assert is_compound_word("hellolumberjack", {"hello", "jack", "lumber", "hellolumberjack"})
    print("Test passed ")
