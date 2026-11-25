"""Exercise 4-6: add commands for handling variables to the calculator.

'_' stores the top of the stack into the next variable (a, b, c, ...),
a lowercase letter pushes the value of that variable.
Uppercase commands: E (exp), H (head), D (duplicate), S (swap), C (clear).
"""
import math
import sys

MAXVAL = 100
NUMBER = "0"
EOF = None

VARSET = "_"
VARGET = "a"
VARNUM = 26

var = "0"
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


def is_empty():
    return not stack


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
    global var
    c = getch()
    while c in (" ", "\t"):
        c = getch()

    if c is EOF:
        return EOF, ""

    if c.islower():
        var = c
        return VARGET, c

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
    var_buff = []

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
        elif type_ == "^":
            op2 = pop()
            push(math.pow(pop(), op2))
        elif type_ == "~":
            push(math.sin(pop()))
        elif type_ == "E":
            push(math.exp(pop()))
        elif type_ == "H":
            view_head()
        elif type_ == "D":
            duplicate()
        elif type_ == "S":
            swap()
        elif type_ == "C":
            clear()
        elif type_ == VARSET:
            if len(var_buff) < VARNUM:
                var_buff.append(pop())
                print("variable %s: %.3f"
                      % (chr(ord("a") + len(var_buff) - 1), var_buff[-1]))
            else:
                print("Error: too many variables.")
        elif type_ == VARGET:
            # Check if the variable has been assigned previously
            idx = ord(var) - ord("a")
            if idx < len(var_buff):
                push(var_buff[idx])
            else:
                print("Error: undefined variable.")
        elif type_ == "\n":
            if not is_empty():
                print("result: %.8g" % pop())
        else:
            print("Error: unknown command %s." % s)


if __name__ == "__main__":
    main()
