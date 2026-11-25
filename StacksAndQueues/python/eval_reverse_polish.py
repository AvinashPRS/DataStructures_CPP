"""
Given a reverse polish expression, evaluate it. In simple terms operators are placed after the operands for each operation
in reverse polish.
Input: string
Output: int

Solution:
    This can be done using a stack. We start scanning from left to right. If we encounter a number we push it to
    the stack. If we get an operator (/, *, +, -) we pop the top two operands from stack, apply the operator and again
    push the result.

    TC: O(n), n: no. of elements
"""


def evaluate_reverse_polish(expr):
    """Returns the reverse polish result."""
    delimiter = ","
    operands = []

    for token in expr.split(delimiter):
        if token in ("*", "/", "-", "+"):
            # The top element is the RIGHT operand
            right = operands.pop()
            # The next element is the LEFT operand
            left = operands.pop()

            if token == "*":
                operands.append(left * right)
            elif token == "/":
                # integer division truncating towards zero (same as C++)
                operands.append(int(left / right))
            elif token == "+":
                operands.append(left + right)
            elif token == "-":
                operands.append(left - right)
        else:
            operands.append(int(token))

    return operands[-1]


if __name__ == "__main__":
    # Evaluates as 3 + 4 = 7
    expr1 = "3,4,+"
    print(f"{expr1} = {evaluate_reverse_polish(expr1)}")

    # Evaluates as 3 - 4 = -1
    expr2 = "3,4,-"
    print(f"{expr2} = {evaluate_reverse_polish(expr2)}")
