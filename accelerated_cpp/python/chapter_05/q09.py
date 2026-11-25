# Chapter 5, exercise 9: write all-lowercase words first, then the rest.
import sys


def is_all_lower(word):
    return not any(c.isupper() for c in word)


def main():
    lower, upper = [], []
    for word in sys.stdin.read().split():
        (lower if is_all_lower(word) else upper).append(word)
    print(" ".join(lower + upper))


if __name__ == "__main__":
    main()
