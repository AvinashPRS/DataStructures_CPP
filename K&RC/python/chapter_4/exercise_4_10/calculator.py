"""Exercise 4-10: calculator that reads an entire input line with getline
instead of using getch and ungetch."""
import math
import sys

MAXVAL = 100
NUMBER = "0"
VARSET = "_"
VARGET = "a"
VARNUM = 26
END = "\0"

var = "0"
line = ""
line_i = 0
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


def next_char():
    global line_i
    c = line[line_i] if line_i < len(line) else END
    line_i += 1
    return c


def getop():
    global var, line_i
    c = next_char()
    while c in (" ", "\t"):
        c = next_char()

    if c.isalpha():
        var = c
        return VARGET, c

    if not c.isdigit() and c != "." and c != "-":
        return c, c

    s = [c]
    if c == "-":
        nxt = next_char()
        if nxt in ("\n", " ", "\t", END):
            line_i -= 1
            return "-", "-"
        if not nxt.isdigit() and nxt != ".":
            return nxt, nxt
        s.append(nxt)
        c = nxt

    if c.isdigit():
        c = next_char()
        while c.isdigit():
            s.append(c)
            c = next_char()

    if c == ".":
        if s[-1] != ".":
            s.append(c)
        c = next_char()
        while c.isdigit():
            s.append(c)
            c = next_char()

    line_i -= 1
    return NUMBER, "".join(s)


def main():
    global line, line_i
    var_buff = [0.0] * VARNUM
    varindex = 0

    for line in sys.stdin:
        line_i = 0
        while True:
            type_, s = getop()
            if type_ == END:
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
            elif type_ == "e":
                push(math.exp(pop()))
            elif type_ == "h":
                view_head()
            elif type_ == "d":
                duplicate()
            elif type_ == "s":
                swap()
            elif type_ == "c":
                clear()
            elif type_ == VARSET:
                if varindex < VARNUM:
                    var_buff[varindex] = pop()
                    varindex += 1
                    print("variable %s: %.3f" % (chr(ord("a") + varindex - 1),
                                                 var_buff[varindex - 1]))
            elif type_ == VARGET:
                push(var_buff[(ord(var) - ord("a")) % VARNUM])
            elif type_ == "\n":
                if not is_empty():
                    print("result: %.8g" % pop())
            else:
                print("Error: unknown command %s." % s)


if __name__ == "__main__":
    main()

# NOTE: Because the operators 'e', 'h', 'd', 's', 'c' are letters, they are
# read as variables by getop (same behaviour as the C version).
