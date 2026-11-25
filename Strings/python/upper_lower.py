"""
Read words from standard input; write all lowercase words first, then the
words that contain uppercase letters.

Usage: echo "Hello world Foo bar" | python3 upper_lower.py
"""
import sys


def is_all_lower(word):
    # look at all the chars
    return not any(c.isupper() for c in word)


def main():
    upper = []
    lower = []
    # read all input
    for word in sys.stdin.read().split():
        (lower if is_all_lower(word) else upper).append(word)

    # write all lowercase words, then words that contain uppercase
    print("".join(w + " " for w in lower + upper))


if __name__ == "__main__":
    main()
