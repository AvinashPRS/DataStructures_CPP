"""Exercise 1-17: print all input lines longer than 80 characters."""
import sys

LIMIT = 80


def main():
    for line in sys.stdin:
        if len(line) > LIMIT:
            sys.stdout.write(line)


if __name__ == "__main__":
    main()
