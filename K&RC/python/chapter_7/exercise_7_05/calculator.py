"""Exercise 7-5: postfix calculator that uses scanf-style input to do the
input and number conversion.

run: python3 calculator.py <<< "2 3 4 2 - + +"
"""
import math
import sys

STACK_MAX_SIZE = 100
stack = []


def push(f):
    if len(stack) < STACK_MAX_SIZE:
        stack.append(f)
    else:
        print("Error: stack full, can't push %g." % f)


def pop():
    if stack:
        return stack.pop()
    print("Error: stack empty.")
    return 0.0


def main():
    for token in sys.stdin.read().split():
        try:
            push(float(token))
            continue
        except ValueError:
            pass

        c = token[0]
        if c == "+":
            push(pop() + pop())
        elif c == "-":
            op2 = pop()
            push(pop() - op2)
        elif c == "*":
            push(pop() * pop())
        elif c == "/":
            op2 = pop()
            if op2 != 0.0:
                push(pop() / op2)
            else:
                print("Error: zero divisor.")
        elif c == "%":
            op2 = pop()
            if op2 != 0.0:
                push(float(int(math.fmod(int(pop()), int(op2)))))
            else:
                print("Error: zero divisor.")
        else:
            print("Error: unknown command.")

    print("result: %.8g" % pop())


if __name__ == "__main__":
    main()
