"""Evaluate an arithmetic expression with + - * / and parentheses."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def compute(num_stack, operator_stack):
    """Apply the top operator to the top two values and push the result."""
    c = operator_stack.pop()
    # Since stack is LIFO we first pop value2 and then value1
    value2 = num_stack.pop()
    value1 = num_stack.pop()
    if c == "+":
        num_stack.append(value1 + value2)
    elif c == "-":
        num_stack.append(value1 - value2)
    elif c == "*":
        num_stack.append(value1 * value2)
    elif c == "/":
        num_stack.append(int(value1 / value2))  # truncate toward zero like C


def is_eq_or_grt_precedence(stack_operator, exp_operator):
    """True if the stack operator has equal or greater precedence."""
    if stack_operator in "*/" and exp_operator in "+-":
        return True
    return stack_operator == exp_operator


def evaluate_expression(expression):
    num_stack = []
    operator_stack = []
    i = 0
    length = len(expression)
    while i < length:
        ch = expression[i]
        if ch in " \t\n":
            i += 1
            continue
        if ch.isdigit():
            start = i
            while i < length and expression[i].isdigit():
                i += 1
            num_stack.append(int(expression[start:i]))
        elif ch == "(":
            operator_stack.append(ch)
            i += 1
        elif ch == ")":
            # Till we encounter '(', process the two stacks
            while operator_stack[-1] != "(":
                compute(num_stack, operator_stack)
            operator_stack.pop()  # pop out '('
            i += 1
        elif ch in "+-*/":
            # While the stack operator has higher precedence, keep processing
            while operator_stack and \
                    is_eq_or_grt_precedence(operator_stack[-1], ch):
                compute(num_stack, operator_stack)
            operator_stack.append(ch)
            i += 1
        else:
            i += 1

    # Process the remaining operators
    while operator_stack:
        compute(num_stack, operator_stack)
    return num_stack[-1]


def test(expression, expected_result):
    result = evaluate_expression(expression)
    print(f"{expression} = {result}")
    if result != expected_result:
        handle_error()


def main():
    test("20 * 40", 800)
    test("10 + 10 * 40", 410)
    test("(200 - (100 + 50)) * 30 / 10", 150)
    test("2 - 6 - 7", -11)
    test("2 + 5 - 1", 6)
    test("5 * 6 + 40", 70)
    test("7 / 10 * 100 + 87", 87)
    print("Test passed ")


if __name__ == "__main__":
    main()
