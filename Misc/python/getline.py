"""
Exercise 2-2. Write a loop equivalent to the for loop below without using
&& or ||:

    for (i=0; i < lim-1 && (c=getchar()) != '\n' && c != EOF; ++i)
        s[i] = c;
"""
import sys

MAXLINE = 1000


def get_line(lim):
    """Read a line (up to lim - 1 chars, keeping the newline)."""
    s = []
    c = ""
    halt = False
    while not halt:
        if len(s) > lim - 1:
            halt = True
        else:
            c = sys.stdin.read(1)
            if c == "\n":
                halt = True
            elif c == "":  # EOF
                halt = True
            else:
                s.append(c)
    if c == "\n":
        s.append(c)
    return "".join(s)


def main():
    while True:
        line = get_line(MAXLINE)
        if len(line) == 0:
            break
        sys.stdout.write(f"line has the chars: {line}")


if __name__ == "__main__":
    main()
