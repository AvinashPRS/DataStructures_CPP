"""Exercise 1-16: print the length of arbitrarily long input lines and the
longest line (as much of it as fits in MAXLINE)."""
import sys

MAXLINE = 1000


def get_line(maxline):
    """Read a line; return (stored_text, real_length).

    Only maxline - 1 characters are stored but the full length is counted.
    """
    line = sys.stdin.readline()
    length = len(line)
    stored = line[:maxline - 1]
    if line.endswith("\n") and not stored.endswith("\n"):
        stored += "\n"
    return stored, length


def main():
    maxlen = 0
    maxline = ""

    while True:
        line, length = get_line(MAXLINE)
        if length <= 0:
            break
        if maxlen < length:
            maxlen = length
            maxline = line
        print("line_length: %d" % length)

    if maxlen > 0:
        sys.stdout.write(maxline)


if __name__ == "__main__":
    main()
