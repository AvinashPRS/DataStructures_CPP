"""
Exercise 2-10. Rewrite the function lower, which converts upper case letters
to lower case, with a conditional expression instead of if-else.
"""
import sys


def lower(c):
    """Convert c to lower case; ASCII only."""
    return chr(ord(c) + ord("a") - ord("A")) if "A" <= c <= "Z" else c


def main():
    for c in iter(lambda: sys.stdin.read(1), ""):
        sys.stdout.write(lower(c))


if __name__ == "__main__":
    main()
