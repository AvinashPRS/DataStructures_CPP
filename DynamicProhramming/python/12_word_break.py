"""Check if a string can be broken into 2 or more dictionary words."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_result(str1, word_start):
    """
    Helper function to print the words present in the string.
    word_start: if the substring from position i to position j of the original
        string is a word in dictionary, then word_start[j] will be i
    """
    pos = len(str1) - 1
    while pos >= 0:
        # The current word ends at pos and starts at word_start[pos]
        print(str1[word_start[pos]:pos + 1], end=" ")
        pos = word_start[pos] - 1


def word_break(str1, dictionary):
    """
    str1: string that we need to check if it can be broken
    dictionary: set of permitted words
    Return value: True if we can break str1 into words in the dictionary
    """
    length = len(str1)
    if length == 0:
        return False

    # if we can break the string from 0 to pos, then is_break_possible[pos] is True
    is_break_possible = [False] * length

    # if the substring from position i to position j is a word in dictionary,
    # then word_start[j] will be i
    word_start = [-1] * length

    for i in range(length):
        # Check if the substring from 0 to i is in the dictionary
        if not is_break_possible[i] and str1[:i + 1] in dictionary:
            is_break_possible[i] = True
            word_start[i] = 0

        # If we can break the substring upto i into dictionary words, then check
        # if all substrings starting from i+1 can be broken into dictionary words
        if is_break_possible[i]:
            for j in range(i + 1, length):
                if not is_break_possible[j] and str1[i + 1:j + 1] in dictionary:
                    # We can form a word from i+1 to j
                    is_break_possible[j] = True
                    word_start[j] = i + 1

    # If word_start[length-1] is 0, the entire input word is in the dictionary.
    # We want a compound word with 2 or more dictionary words, so check != 0
    result = is_break_possible[length - 1] and word_start[length - 1] != 0

    if result:
        print_result(str1, word_start)

    return result


def test(str1, expected_result):
    dictionary = {"i", "will", "play", "now"}

    print(f"{str1} => ", end="")
    result = word_break(str1, dictionary)
    print()

    if result:
        print(f"{str1} can be broken ")
    else:
        print(f"{str1} cannot be broken ")

    if result != expected_result:
        handle_error()

    print("________________________________________")


if __name__ == "__main__":
    test("iwilli", True)
    test("iwillplaynow", True)
    test("nowplayiwill", True)
    test("iiiiiiiiiii", True)
    test("iwpn", False)
    print("Test passed ")
