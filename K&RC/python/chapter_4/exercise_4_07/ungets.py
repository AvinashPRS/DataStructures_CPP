"""Exercise 4-7: ungets(s) pushes back an entire string onto the input."""
import sys

BUFFSIZE = 1000
buf = []


def getch():
    if buf:
        return buf.pop()
    return sys.stdin.read(1)  # "" means EOF


def ungetch(c):
    if len(buf) >= BUFFSIZE:
        print("ungetch: too many characters")
    else:
        buf.append(c)


def getstr():
    line = []
    while True:
        c = getch()
        if c == "" or c == "\n":
            break
        line.append(c)
    if c == "\n":
        line.append(c)
    return "".join(line)


def ungetstr(line):
    for c in reversed(line):
        ungetch(c)


def main():
    line = getstr()
    sys.stdout.write(line)

    ungetstr(line)

    temp = getstr()
    sys.stdout.write(temp)


if __name__ == "__main__":
    main()

# NOTE: ungetstr() doesn't need access to buf; using ungetch() is enough.
