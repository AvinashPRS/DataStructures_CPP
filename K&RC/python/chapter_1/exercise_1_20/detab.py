"""Exercise 1-20: replace tabs in the input with blanks."""
import sys

TAB_LENGTH = 8


def main():
    out = sys.stdout
    for c in sys.stdin.read():
        if c == "\t":
            out.write(" " * TAB_LENGTH)
        else:
            out.write(c)


if __name__ == "__main__":
    main()

# NOTE: run: python3 detab.py < file_in.txt > file_out.txt
