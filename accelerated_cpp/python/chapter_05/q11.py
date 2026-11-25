# Chapter 5, exercise 11: words with ascenders/descenders, and the longest
# word that has neither.
import sys

ASCENDERS_DESCENDERS = set("bdfhklgjpqy")


def has_ascender_or_descender(s):
    return any(c in ASCENDERS_DESCENDERS for c in s)


def main():
    words = []
    longest_word = ""
    for word in sys.stdin.read().split():
        if has_ascender_or_descender(word):
            words.append(word)
        elif len(word) > len(longest_word):
            longest_word = word

    print("The word(s) that have ascenders or descenders are: " + ", ".join(words))
    print('The longest word that does not have ascenders or descenders is '
          f'"{longest_word}" with {len(longest_word)} letters.')


if __name__ == "__main__":
    main()
