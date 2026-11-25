"""Exercise 1-11: word count program (count lines, words and characters).

Test it with: empty input, only blanks, one very long word, words separated
by several kinds of whitespace, etc.
"""
import sys

IN = 1
OUT = 0


def main():
    nl = nw = nc = 0
    state = OUT

    for c in sys.stdin.read():
        nc += 1

        if c == "\n":
            nl += 1

        if c in (" ", "\n", "\t"):
            state = OUT
        elif state == OUT:
            state = IN
            nw += 1

    print("lines: %d\nwords: %d\ncharacters: %d" % (nl, nw, nc))


if __name__ == "__main__":
    main()
