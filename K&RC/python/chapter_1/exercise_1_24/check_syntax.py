"""Exercise 1-24: check a C program for rudimentary syntax errors like
unbalanced parentheses, brackets, braces, quotes and comments."""
import sys


def check_syntax(s):
    parentheses = brackets = braces = 0
    single_quotes = double_quotes = False
    block_comment = line_comment = False
    n = len(s)

    def at(k):
        return s[k] if 0 <= k < n else "\0"

    i = 0
    while i < n and parentheses >= 0 and brackets >= 0 and braces >= 0:
        c = s[i]
        if not (line_comment or block_comment or single_quotes or double_quotes):
            if c == "(":
                parentheses += 1
            elif c == ")":
                parentheses -= 1
            if c == "[":
                brackets += 1
            elif c == "]":
                brackets -= 1
            if c == "{":
                braces += 1
            elif c == "}":
                braces -= 1

        if not line_comment and not block_comment:
            escaped = at(i - 1) == "\\" and at(i - 2) != "\\"
            if c == "'" and not single_quotes and not double_quotes:
                single_quotes = True
            elif single_quotes and c == "'" and not escaped:
                single_quotes = False

            if c == '"' and not single_quotes and not double_quotes:
                double_quotes = True
            elif double_quotes and c == '"' and not escaped:
                double_quotes = False

        if not single_quotes and not double_quotes:
            if c == "/" and at(i + 1) == "*" and not line_comment:
                block_comment = True
            elif c == "*" and at(i + 1) == "/":
                block_comment = False

            if c == "/" and at(i + 1) == "/" and not block_comment:
                line_comment = True
            elif c == "\n":
                line_comment = False

        i += 1

    if parentheses:
        print("Error: unbalanced parentheses.")
    if brackets:
        print("Error: unbalanced brackets.")
    if braces:
        print("Error: unbalanced braces.")
    if single_quotes:
        print("Error: unbalanced single quotes.")
    if double_quotes:
        print("Error: unbalanced double quotes.")
    if block_comment:
        print("Error: block comment not closed.")


def main():
    check_syntax(sys.stdin.read())


if __name__ == "__main__":
    main()
