"""Exercise 1-22: fold long input lines into two or more shorter lines."""
import sys

BREAKING_POINT = 40
OFFSET = 10


def fold_line(line, n_break):
    fold = []
    column = 0
    split = False
    last_blank = 0

    for ch in line:
        fold.append(ch)
        j = len(fold) - 1

        if ch == "\n":
            column = 0

        column += 1

        if column == n_break - OFFSET:
            split = True

        if split and ch in (" ", "\t"):
            last_blank = j

        if column == n_break:
            if last_blank:
                fold[last_blank] = "\n"
                column = j - last_blank
                last_blank = 0
            else:
                # Hard break: the current char is replaced by a hyphen
                # followed by a newline (same as the C version)
                fold[j] = "-"
                fold.append("\n")
                column = 0
            split = False

    return "".join(fold)


def main():
    for line in sys.stdin:
        sys.stdout.write(fold_line(line, BREAKING_POINT))


if __name__ == "__main__":
    main()
