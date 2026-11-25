"""
Counts the number of alphabetical words in a string.
A new word is detected whenever a non-alphabet character transitions to an alphabet character.
"""
import sys


def handle_error():
    print("Test failed", file=sys.stderr)
    sys.exit(1)


def count_words(s):
    num_words = 0
    is_prev_char_alphabet = False

    for c in s:
        is_cur_char_alphabet = c.isalpha()

        if not is_prev_char_alphabet and is_cur_char_alphabet:
            num_words += 1

        is_prev_char_alphabet = is_cur_char_alphabet

    return num_words


def test(s, expected_result):
    result = count_words(s)

    if result != expected_result:
        handle_error()

    print(f'Word count = {result}, for string: "{s}"')


if __name__ == "__main__":
    test("hello", 1)
    test("", 0)
    test("   hello,how are    you doing?", 5)

    print("Test passed")
