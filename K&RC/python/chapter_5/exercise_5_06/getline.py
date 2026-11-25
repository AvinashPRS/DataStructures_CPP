"""Exercise 5-6: get_line rewritten with pointers."""
import sys


def get_line():
    chars = []
    while True:
        c = sys.stdin.read(1)
        if c == "" or c == "\n":
            break
        chars.append(c)
    return "".join(chars)


def main():
    print(get_line())


if __name__ == "__main__":
    main()
