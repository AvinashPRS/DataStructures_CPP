"""Exercise 2-10: lower() using a conditional expression."""
import sys


def lower(c):
    return chr(ord(c) + ord("a") - ord("A")) if "A" <= c <= "Z" else c


def main():
    a = "A"
    sys.stdout.write(lower(a))


if __name__ == "__main__":
    main()

# NOTE: The conditional expression can be used directly in return.
