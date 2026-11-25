"""Exercise 4-4: calculator commands to print the top of the stack (h),
duplicate it (d), swap the top two elements (s) and clear the stack (c)."""
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
        print("Error: stack full.")


def pop():
    if stack:
        return stack.pop()
    print("Error: stack empty.")
    return 0.0


def view_head():
    if stack:
        print("stack_head: %g" % stack[-1])
    else:
        print("Error: stack empty.")


def duplicate():
    temp = pop()
    push(temp)
    push(temp)


def swap():
    temp1 = pop()
    temp2 = pop()
    push(temp1)
    push(temp2)


def clear():
    stack.clear()


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
            return "-", "-"
        if not isdigit(nxt) and nxt != ".":
            return nxt, nxt or ""
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
        elif type_ == "h":
            view_head()
        elif type_ == "d":
            duplicate()
        elif type_ == "s":
            swap()
        elif type_ == "c":
            clear()
        elif type_ == "\n":
            print("result: %.8g" % pop())
        else:
            print("Error: unknown command %s." % s)


if __name__ == "__main__":
    main()
