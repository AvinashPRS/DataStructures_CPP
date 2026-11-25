"""Exercise 5-2: getfloat, the floating point analog of getint."""
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


def isdigit(c):
    return c is not None and c.isdigit()


def getfloat():
    """Return (status, number)."""
    c = getch()
    while c is not EOF and c.isspace():
        c = getch()

    if not isdigit(c) and c is not EOF and c not in "+-.":
        ungetch(c)
        return 0, 0.0

    sign = -1 if c == "-" else 1

    if c in ("+", "-"):
        c = getch()
        if not isdigit(c):
            if c is not EOF:
                ungetch(c)
            ungetch("+" if sign == 1 else "-")
            return 0, 0.0

    n = 0.0
    while isdigit(c):
        n = 10 * n + (ord(c) - ord("0"))
        c = getch()

    if c == ".":
        i = 1
        c = getch()
        while isdigit(c):
            n += (ord(c) - ord("0")) / (10 ** i)
            i += 1
            c = getch()

    n *= sign

    if c is not EOF:
        ungetch(c)

    return c, n


def main():
    _, number = getfloat()
    print("number: %f" % number)


if __name__ == "__main__":
    main()

# NOTE: getfloat() returns the status like getint(); the value is returned
# as the second element of the tuple (Python has no pointer arguments).
