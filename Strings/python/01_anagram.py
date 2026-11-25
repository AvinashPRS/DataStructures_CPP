"""
An anagram is a word, phrase, or sentence formed by rearranging the letters of another word,
phrase, or sentence, using all the original letters exactly once
"""
import sys

NUM_CHARACTERS = 256


def handle_error():
    print("Test failed")
    sys.exit(1)


def are_strings_anagrams(str1, str2):
    """
    str1, str2: the two strings which we want to compare
    Returns: True if the two strings are anagrams, False otherwise
    """
    count1 = [0] * NUM_CHARACTERS
    count2 = [0] * NUM_CHARACTERS

    # Compute the character counts for str1 and str2
    for c in str1:
        count1[ord(c)] += 1
    for c in str2:
        count2[ord(c)] += 1

    # Compare the counts
    return count1 == count2


def test(s1, s2, expected_result):
    result = are_strings_anagrams(s1, s2)

    print(f"{s1} and {s2} are ", end="")
    print("anagrams" if result else "not anagrams")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("ABCDE", "CDBAE", True)
    test("AAAAA", "BBBBB", False)

    print("Test passed ")
