"""Exercise 5-10: expr evaluates a reverse Polish expression from the
command line, where each operator or operand is a separate argument.

    python3 expr.py 2 3 4 + '*'
"""
import sys

STACK_SIZE = 15
stack = []


def pop():
    if stack:
        return stack.pop()
    print("Error: the stack is empty.")
    return 0.0


def push(element):
    if len(stack) < STACK_SIZE:
        stack.append(element)
    else:
        print("Error: the stack is full.")


def to_number(arg):
    try:
        return float(arg)
    except ValueError:
        return None


def main(argv):
    error = 0

    for arg in argv[1:]:
        number = to_number(arg)

        if number is not None:
            push(number)
        elif len(arg) == 1:
            if 2 <= len(stack) < STACK_SIZE:
                number2 = pop()
                number1 = pop()

                if arg == "+":
                    push(number1 + number2)
                elif arg == "-":
                    push(number1 - number2)
                elif arg == "*":  # might need escaping in the shell
                    push(number1 * number2)
                elif arg == "/":
                    if number2 == 0:
                        error = 4
                    else:
                        push(number1 / number2)
                else:
                    error = 3
            else:
                error = 2
        else:
            error = 1

    if error:
        messages = {
            1: "Error: arguments should be numbers or one of the following "
               "mathematical operations: '+', '-', '*', '/'.",
            2: "Error: too many or too few arguments.",
            3: "Error: invalid operation. use one of the following "
               "mathematical operations: '+', '-', '*', '/'.",
            4: "Error: division by zero (NaN).",
        }
        print(messages[error])
        return 1

    print("result: %.3f" % pop(), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
