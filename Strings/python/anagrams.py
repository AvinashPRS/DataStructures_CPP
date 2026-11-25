"""
An anagram is a word, phrase, or sentence formed by rearranging the letters of another word,
phrase, or sentence, using all the original letters exactly once

Pythonic version: collections.Counter does the character counting and
comparing two Counters checks that every character count matches.
"""
import sys
from collections import Counter


def handle_error():
    print("Test failed")
    sys.exit(1)


def are_strings_anagrams(str1, str2):
    """
    str1, str2: the two strings we want to compare
    Returns: True if the two strings are anagrams, False otherwise
    """
    return Counter(str1) == Counter(str2)


def test(s1, s2, expected_result):
    result = are_strings_anagrams(s1, s2)

    print(f"{s1} and {s2} are ", end="")
    print("anagrams" if result else "not anagrams")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("ABCDE", "CDBAE", True)
    test("AAAAA", "BBBBB", False)

    print("Test passed")
