"""Exercise 1-10: replace tab, backspace and backslash by \\t, \\b and \\\\."""
import sys


def main():
    out = sys.stdout
    while True:
        c = sys.stdin.read(1)
        if c == "":
            break
        if c == "\t":
            out.write("\\t")
        elif c == "\b":
            out.write("\\b")
        elif c == "\\":
            out.write("\\\\")
        else:
            out.write(c)


if __name__ == "__main__":
    main()
