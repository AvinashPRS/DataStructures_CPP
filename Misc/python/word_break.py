"""Word break: can a string be split into 2+ dictionary words? Prints the words."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def print_result(str1, word_start):
    """Print the words from the end of the string back to the start.
    word_start[j] = i means str1[i..j] is a dictionary word."""
    out = []
    pos = len(str1) - 1
    while pos >= 0:
        out.append(str1[word_start[pos]:pos + 1] + " ")
        pos = word_start[pos] - 1
    print("".join(out), end="")


def word_break(str1, dictionary):
    length = len(str1)
    if length == 0:
        return False

    # is_break_possible[pos]: str1[0..pos] can be broken into words
    is_break_possible = [False] * length
    # word_start[j] = i if str1[i..j] is a dictionary word
    word_start = [-1] * length

    for i in range(length):
        # Is the substring from 0 to i in the dictionary?
        if not is_break_possible[i] and str1[:i + 1] in dictionary:
            is_break_possible[i] = True
            word_start[i] = 0

        # If str1[0..i] can be broken, try words starting at i + 1
        if is_break_possible[i]:
            for j in range(i + 1, length):
                if not is_break_possible[j] and str1[i + 1:j + 1] in dictionary:
                    is_break_possible[j] = True
                    word_start[j] = i + 1

    # word_start[length-1] == 0 means the whole string is one word;
    # we want 2 or more words
    result = is_break_possible[length - 1] and word_start[length - 1] != 0
    if result:
        print_result(str1, word_start)
    return result


def test(str1, expected_result):
    dictionary = {"i", "will", "play", "now"}
    print(f"{str1} => ", end="")
    result = word_break(str1, dictionary)
    print()
    print(f"{str1} can be broken " if result else f"{str1} cannot be broken ")
    if result != expected_result:
        handle_error()
    print("________________________________________")


def main():
    test("iwilli", True)
    test("iwillplaynow", True)
    test("nowplayiwill", True)
    test("iiiiiiiiiii", True)
    test("iwpn", False)
    print("Test passed ")


if __name__ == "__main__":
    main()
