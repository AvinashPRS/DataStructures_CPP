"""Exercise 5-6: getop rewritten with pointers."""
import sys

NUMBER = 0


class Input:
    def __init__(self, stream):
        self.stream = stream
        self.pushed = []

    def getchar(self):
        if self.pushed:
            return self.pushed.pop()
        return self.stream.read(1)

    def ungetc(self, c):
        self.pushed.append(c)


def getop(inp):
    """Return (type, token)."""
    c = inp.getchar()
    # Skip blanks (spaces and tabs)
    while c in (" ", "\t"):
        c = inp.getchar()

    # Not a number
    if not c.isdigit() and c != ".":
        return (ord(c) if c else -1), c

    s = [c]
    # Collect the integer part
    if c.isdigit():
        c = inp.getchar()
        while c.isdigit():
            s.append(c)
            c = inp.getchar()

    # Collect the fraction part
    if c == ".":
        if s[-1] != ".":
            s.append(c)
        c = inp.getchar()
        while c.isdigit():
            s.append(c)
            c = inp.getchar()

    if c != "":
        inp.ungetc(c)

    return NUMBER, "".join(s)


def main():
    type_, s = getop(Input(sys.stdin))
    print("%d %s" % (type_, s))


if __name__ == "__main__":
    main()
