"""Exercise 1-19: reverse each input line, one line at a time."""
import sys

MAXLINE = 1000


def reverse(line):
    """Reverse the characters of a line, keeping a trailing newline in place."""
    chars = list(line)
    i_front = 0
    i_back = len(chars) - (2 if chars and chars[-1] == "\n" else 1)

    while i_back > i_front:
        chars[i_front], chars[i_back] = chars[i_back], chars[i_front]
        i_front += 1
        i_back -= 1

    return "".join(chars)


def main():
    for line in sys.stdin:
        # Lines exceeding the limit are truncated, as in the C version
        if len(line) > MAXLINE - 1:
            line = line[:MAXLINE - 2] + ("\n" if line.endswith("\n") else "")
        sys.stdout.write(reverse(line))


if __name__ == "__main__":
    main()
