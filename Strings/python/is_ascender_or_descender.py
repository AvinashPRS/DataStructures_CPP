"""
Read words from standard input; report the words that have ascenders or
descenders and the longest word that has neither.

Usage: echo "hello world mouse cream" | python3 is_ascender_or_descender.py
"""
import sys

ASCENDERS_DESCENDERS = set("bdfhklgjpqy")


def is_ascender_or_descender(c):
    return c in ASCENDERS_DESCENDERS


def has_ascender_or_descender(s):
    # search all characters
    return any(is_ascender_or_descender(c) for c in s)


def main():
    words = []
    longest_word = ""
    max_length = 0

    # read all input
    for word in sys.stdin.read().split():
        if has_ascender_or_descender(word):
            words.append(word)
        elif len(word) > max_length:
            # update the longest word
            longest_word = word
            max_length = len(word)

    print("The word(s) that have ascenders or descenders are: " + ", ".join(words))
    print(f'The longest word that does not have ascenders or descenders is '
          f'"{longest_word}" with {max_length} letters.')


if __name__ == "__main__":
    main()
