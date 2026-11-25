"""Exercise 1-9: copy input to output replacing runs of blanks by one blank."""
import sys


def main():
    last_c = "\0"
    out = sys.stdout

    while True:
        c = sys.stdin.read(1)
        if c == "":
            break
        if c != " " or last_c != " ":
            out.write(c)
        last_c = c


if __name__ == "__main__":
    main()
