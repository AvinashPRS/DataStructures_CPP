"""Fill in + / - operators between numbers so the equation equals rhs."""
import sys


def handle_error():
    print("Test failed ")
    sys.exit(1)


def evaluate(a, operators):
    """Evaluates the numbers in a with operators applied between them."""
    result = a[0]
    for i in range(1, len(a)):
        if operators[i - 1] == "+":
            result += a[i]
        else:
            result -= a[i]
    return result


def fill_operators(a, rhs, operators, num_operators):
    """
    a: list of numbers (len >= 1)
    rhs: right hand side of the equation
    operators: list for storing the operators applied on the numbers
    num_operators: number of operators that have been filled so far
    Returns True if we can obtain rhs by placing operators between numbers.
    """
    n = len(a)
    if num_operators == n - 1:
        # All operators filled. Evaluate and terminate the recursion
        return evaluate(a, operators) == rhs

    # Fill in + as the next operator and try out
    operators[num_operators] = "+"
    if fill_operators(a, rhs, operators, num_operators + 1):
        return True

    # Fill in - as the next operator and try out
    operators[num_operators] = "-"
    return fill_operators(a, rhs, operators, num_operators + 1)


def test():
    a = [10, 20, 30]
    n = len(a)
    operators = [""] * n
    rhs = -40

    is_possible = fill_operators(a, rhs, operators, 0)

    # We should be able to get -40 since 10 - 20 - 30 = -40
    if not is_possible:
        handle_error()

    out = f"{a[0]} "
    for i in range(1, n):
        out += f"{operators[i - 1]} {a[i]} "
    print(out + f" = {rhs} ")
    print()


def main():
    test()
    print("Test passed")


if __name__ == "__main__":
    main()
