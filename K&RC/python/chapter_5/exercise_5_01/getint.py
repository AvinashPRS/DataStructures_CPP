"""Exercise 5-1: getint that treats a + or - not followed by a digit as not
a number and pushes it back on the input."""
import sys

BUFFSIZE = 100
EOF = None
buf = []


def printbuf():
    if buf:
        items = ["'%s'" % (c if c != "\n" else ".") for c in reversed(buf)
                 if c is not EOF]
        print("Buffer: [ " + ", ".join(items) + " ]")


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


def isdigit(c):
    return c is not None and c.isdigit()


def getint():
    """Return (status, number). status is 0 if the input is not a number,
    EOF at end of file, otherwise the next character."""
    c = getch()
    while c is not EOF and c.isspace():
        c = getch()

    if not isdigit(c) and c is not EOF and c not in "+-":
        ungetch(c)
        return 0, 0

    sign = -1 if c == "-" else 1

    if c in ("+", "-"):
        c = getch()
        if not isdigit(c):
            if c is not EOF:
                ungetch(c)
            ungetch("+" if sign == 1 else "-")
            return 0, 0

    n = 0
    while isdigit(c):
        n = 10 * n + (ord(c) - ord("0"))
        c = getch()

    n *= sign

    if c is not EOF:
        ungetch(c)

    return c, n


def main():
    _, number = getint()
    print(number)

    printbuf()


if __name__ == "__main__":
    main()
