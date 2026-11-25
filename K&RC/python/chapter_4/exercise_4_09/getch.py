"""Exercise 4-9: getch/ungetch that handle a pushed-back EOF correctly."""
import sys

BUFFSIZE = 100
EOF = None
buf = []


def getch():
    if buf:
        return buf.pop()
    c = sys.stdin.read(1)
    return c if c else EOF


def ungetch(c):
    if len(buf) >= BUFFSIZE:
        print("ungetch: too many characters")
    else:
        buf.append(c)


def putchar(c):
    if c is not EOF:
        sys.stdout.write(c)


def main():
    c = getch()
    putchar(c)

    ungetch(EOF)

    c = getch()
    putchar(c)


if __name__ == "__main__":
    main()

# NOTE: In the original K&R version buf was a char array, which can't portably
# hold EOF (-1). Here EOF is represented by None and the buffer is a list, so
# it can hold it without problems.
