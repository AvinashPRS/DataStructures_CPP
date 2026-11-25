"""Exercise 4-8: getch/ungetch with a single character of pushback."""
import sys

buf = None


def getch():
    global buf
    if buf is not None:
        temp = buf
        buf = None
        return temp
    return sys.stdin.read(1)


def ungetch(c):
    global buf
    if buf is not None:
        print("ungetch: buffer full")
    else:
        buf = c


def main():
    c = getch()
    print(c)

    ungetch(c)

    c = getch()
    print(c)


if __name__ == "__main__":
    main()
