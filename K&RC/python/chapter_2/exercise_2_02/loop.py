"""Exercise 2-2: write the getline loop without using && or ||.

    for (i = 0; i < lim - 1 && (c = getchar()) != '\\n' && c != EOF; ++i)
        s[i] = c;
"""
import sys

MAXLINE = 1000


def main():
    s = []
    i = 0

    while True:
        if i >= MAXLINE - 1:
            break

        c = sys.stdin.read(1)

        if c == "\n":
            break
        elif c == "":  # EOF
            break
        else:
            s.append(c)
            i += 1

    print("".join(s))


if __name__ == "__main__":
    main()
