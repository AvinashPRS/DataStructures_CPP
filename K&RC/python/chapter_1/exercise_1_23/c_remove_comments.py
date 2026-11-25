"""Exercise 1-23: remove all comments from a C program read on stdin."""
import sys


def remove_comments(s):
    in_quote = False
    line_comment = False
    block_comment = False

    out = []
    n = len(s)

    def at(k):
        return s[k] if k < n else "\0"

    i = 0
    while i < n:
        if not block_comment:
            if not in_quote and s[i] == '"':
                in_quote = True
            elif in_quote and s[i] == '"':
                in_quote = False

        if not in_quote:
            if at(i) == "/" and at(i + 1) == "*" and not line_comment:
                block_comment = True

            if at(i) == "*" and at(i + 1) == "/":
                block_comment = False
                i += 2

            if at(i) == "/" and at(i + 1) == "/":
                line_comment = True

            if at(i) == "\n":
                line_comment = False

            if line_comment or block_comment:
                i += 1
            elif i < n:
                out.append(s[i])
                i += 1
        else:
            out.append(s[i])
            i += 1

    return "".join(out)


def main():
    sys.stdout.write(remove_comments(sys.stdin.read()))


if __name__ == "__main__":
    main()

# NOTE: run: python3 c_remove_comments.py < ../../../chapter_1/exercise_1_23/c_remove_comments.c
