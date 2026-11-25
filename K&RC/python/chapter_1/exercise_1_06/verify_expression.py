"""Exercise 1-6: verify that the expression getchar() != EOF is 0 or 1."""
import sys


def main():
    c = sys.stdin.read(1)
    # read() returns "" at end of file (the equivalent of EOF).
    print("value of expression: %d" % int(c != ""), end="")


if __name__ == "__main__":
    main()

# NOTE: The expression is equal to 1 only if the input char is not EOF.
# On Windows EOF is sent with CTRL+Z, on Unix-like systems with CTRL+D.
