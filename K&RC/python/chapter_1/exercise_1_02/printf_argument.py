"""Exercise 1-2: experiment with an unknown escape sequence (\\c)."""
import sys


def main():
    # Python, like C, does not know "\c"; we print the literal backslash + c.
    sys.stdout.write("hello, world\\c")


if __name__ == "__main__":
    main()
