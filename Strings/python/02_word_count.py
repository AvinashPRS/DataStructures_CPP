"""Count the number of words (runs of alphabets) in a string."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def is_alphabet(c):
    """Helper function which checks if a character is an alphabet (a-zA-Z)"""
    return ("A" <= c <= "Z") or ("a" <= c <= "z")


def count_words(str1):
    """
    str1: string in which the number of words have to be counted
    Returns: number of words in the string
    """
    if not str1:
        return 0

    num_words = 0
    is_prev_char_alphabet = False
    for cur_char in str1:
        is_cur_char_alphabet = is_alphabet(cur_char)

        # If previous character is not an alphabet and current character
        # is an alphabet then we have found a new word
        if not is_prev_char_alphabet and is_cur_char_alphabet:
            num_words += 1

        is_prev_char_alphabet = is_cur_char_alphabet

    return num_words


def test(str1, expected_result):
    result = count_words(str1)

    if result != expected_result:
        handle_error()

    print(f"Word count = {result}, for string: {str1}")


if __name__ == "__main__":
    test("hello", 1)
    test("", 0)
    test("   hello,how are    you doing?", 5)

    print("Test passed")
