"""Find the longest word that is made of two or more other words in the list."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_words(words):
    for w in words:
        print(w)


def word_break(str1, dictionary):
    """
    str1: string that we need to check if it can be broken
    dictionary: set of permitted words
    Returns True if str1 can be broken into 2 or more dictionary words.
    """
    length = len(str1)
    if length == 0:
        return False

    # is_break_possible[pos] is True if str1[0..pos] can be broken
    is_break_possible = [False] * length
    # if str1[i..j] is a word in dictionary, then word_start[j] = i
    word_start = [-1] * length

    for i in range(length):
        # Check if the substring from 0 to i is in the dictionary
        if not is_break_possible[i] and str1[:i + 1] in dictionary:
            is_break_possible[i] = True
            word_start[i] = 0

        # If we can break up to i, check all substrings starting from i+1
        if is_break_possible[i]:
            for j in range(i + 1, length):
                if not is_break_possible[j] and str1[i + 1:j + 1] in dictionary:
                    is_break_possible[j] = True
                    word_start[j] = i + 1

    # word_start[length-1] == 0 means the whole word is in the dictionary;
    # we want a compound word with 2 or more dictionary words.
    return is_break_possible[length - 1] and word_start[length - 1] != 0


def find_longest_compound_word(words):
    """Returns the longest compound word if it exists, None otherwise."""
    dictionary = set(words)
    # Sort so that the longest word appears first
    words.sort(key=len, reverse=True)
    for w in words:
        if word_break(w, dictionary):
            return w
    return None


def test_01():
    words = ["hello", "jack", "lumber", "hellolumberjack", "hellojack"]
    print_words(words)
    longest = find_longest_compound_word(words)
    if longest:
        print(f"Longest compound word = {longest}")
    if longest != "hellolumberjack":
        handle_error()
    print("________________________________________")


def test_02():
    words = ["hello", "jack", "lumber"]
    print_words(words)
    longest = find_longest_compound_word(words)
    if longest:
        print(f"Longest compound word = {longest}")
    else:
        print("No compound word possible ")
    if longest is not None:
        handle_error()
    print("________________________________________")


def main():
    test_01()
    test_02()
    print("Test passed ")


if __name__ == "__main__":
    main()
