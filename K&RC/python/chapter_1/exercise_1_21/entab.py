"""Exercise 1-21: replace strings of blanks by the minimum number of tabs and
blanks to achieve the same spacing."""
import sys

TAB_LENGTH = 8


def main():
    out = sys.stdout
    line_pos = 0
    nr_of_spaces = 0

    for c in sys.stdin.read():
        line_pos += 1

        if c == " ":
            nr_of_spaces += 1

            if line_pos % TAB_LENGTH == 0 and nr_of_spaces > 1:
                out.write("\t")
                nr_of_spaces = 0
        else:
            out.write(" " * nr_of_spaces)
            nr_of_spaces = 0

            if c == "\n":
                line_pos = 0

            out.write(c)


if __name__ == "__main__":
    main()

# NOTE: run: python3 entab.py < file_in.txt > file_out.txt
