"""Exercise 4-11: getop that uses an internal static variable instead of
ungetch to remember one character of lookahead."""
import math
import sys

MAXVAL = 100
NUMBER = "0"
EOF = None

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


def getchar():
    c = sys.stdin.read(1)
    return c if c else EOF


def isdigit(c):
    return c is not None and c.isdigit()


def getop(_state={"buf": EOF}):
    """The mutable default argument plays the role of a C static variable."""
    if _state["buf"] is not EOF:
        c = _state["buf"]
        _state["buf"] = EOF
    else:
        c = getchar()

    while c in (" ", "\t"):
        c = getchar()

    if c is EOF:
        return EOF, ""
    if not isdigit(c) and c != "." and c != "-":
        return c, c

    s = [c]
    if c == "-":
        nxt = getchar()
        if nxt in ("\n", " ", "\t", EOF):
            _state["buf"] = nxt
            return "-", "-"
        if not isdigit(nxt) and nxt != ".":
            return nxt, nxt
        s.append(nxt)
        c = nxt

    if isdigit(c):
        c = getchar()
        while isdigit(c):
            s.append(c)
            c = getchar()

    if c == ".":
        if s[-1] != ".":
            s.append(c)
        c = getchar()
        while isdigit(c):
            s.append(c)
            c = getchar()

    if c is not EOF:
        _state["buf"] = c

    return NUMBER, "".join(s)


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
                push(float(int(math.fmod(int(pop()), int(op2)))))
            else:
                print("Error: zero divisor.")
        elif type_ == "\n":
            print("result: %.8g" % pop())
        else:
            print("Error: unknown command %s." % s)


if __name__ == "__main__":
    main()
