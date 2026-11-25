"""Find the first non-repeating (unique) character in a string."""
import sys

MAX_NUM_CHARS = 256


def handle_error():
    print("Error occured")
    sys.exit(1)


def find_first_unique_char(str1):
    """
    str1: string to be searched
    Returns: first unique character if it exists, '' otherwise
    """
    count = [0] * MAX_NUM_CHARS

    # count the number of occurences of each character
    for c in str1:
        count[ord(c)] += 1

    # traverse str1 and find first character which occurs only once
    for c in str1:
        if count[ord(c)] == 1:
            return c

    return ""


def test(str1, expected_result):
    result = find_first_unique_char(str1)

    print(f'First unique in "{str1}" is {result}')

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("aabbbccccddeffffgg", "e")
    test("abcdefab", "c")

    print("Test passed")
