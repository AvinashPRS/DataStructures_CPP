"""Exercise 4-3: reverse Polish calculator with modulus (%) operator and
support for negative numbers."""
import math
import sys

MAXVAL = 100
NUMBER = "0"
EOF = None

# ---------------------------------------------------------------- stack
stack = []


def push(f):
    if len(stack) < MAXVAL:
        stack.append(f)
    else:
        print("Error: stack full, can't push %g." % f)


def pop():
    if stack:
        return stack.pop()
    print("Error: stack empty.")
    return 0.0


# ---------------------------------------------------------- getch/ungetch
buf = []


def getch():
    if buf:
        return buf.pop()
    c = sys.stdin.read(1)
    return c if c else EOF


def ungetch(c):
    buf.append(c)


def isdigit(c):
    return c is not None and c.isdigit()


def getop():
    """Return (type, token_string)."""
    c = getch()
    while c in (" ", "\t"):
        c = getch()

    if c is EOF:
        return EOF, ""
    if not isdigit(c) and c != "." and c != "-":
        return c, c

    s = [c]
    if c == "-":
        nxt = getch()
        if nxt in ("\n", " ", "\t"):
            ungetch(nxt)
            return "-", "-"  # '-' used as operator
        if not isdigit(nxt) and nxt != ".":
            return nxt, nxt or ""  # not a number
        s.append(nxt)
        c = nxt

    if isdigit(c):
        c = getch()
        while isdigit(c):
            s.append(c)
            c = getch()

    if c == ".":
        if s[-1] != ".":
            s.append(c)
        c = getch()
        while isdigit(c):
            s.append(c)
            c = getch()

    if c is not EOF:
        ungetch(c)

    return NUMBER, "".join(s)


def c_fmod(a, b):
    return int(math.fmod(int(a), int(b)))


def main():
    while True:
        type_, s = getop()
        if type_ is EOF:
            break

        if type_ == NUMBER:
            push(float(s))
        elif type_ == "+":
            push(pop() + pop())
        elif type_ == "-":
            op2 = pop()
            push(pop() - op2)
        elif type_ == "*":
            push(pop() * pop())
        elif type_ == "/":
            op2 = pop()
            if op2 != 0.0:
                push(pop() / op2)
            else:
                print("Error: zero divisor.")
        elif type_ == "%":
            op2 = pop()
            if op2 != 0.0:
                push(float(c_fmod(pop(), op2)))
            else:
                print("Error: zero divisor.")
        elif type_ == "\n":
            print("result: %.8g" % pop())
        else:
            print("Error: unknown command %s." % s)


if __name__ == "__main__":
    main()

# NOTE: getch() checks if there are characters in a buffer. If there are it
# returns the last one, otherwise it reads from input. ungetch() pushes a
# character back into the buffer.
