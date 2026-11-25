"""Exercise 1-18: remove trailing blanks and tabs from each input line."""
import sys


def remove_trailing_blanks(line):
    return line.rstrip("\n").rstrip(" \t") + "\n"


def main():
    for line in sys.stdin:
        sys.stdout.write(remove_trailing_blanks(line))


if __name__ == "__main__":
    main()
