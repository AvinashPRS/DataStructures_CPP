"""
Split each line of standard input into whitespace separated words.
(code is taken from Accelerated C++ §5.6/88)

Usage: echo "hello   world  foo" | python3 split.py
"""
import sys


def split(s):
    ret = []
    i = 0
    n = len(s)

    # invariant: we have processed characters [original value of i, i)
    while i != n:
        # ignore leading blanks
        while i != n and s[i].isspace():
            i += 1

        # find end of next word
        j = i
        while j != n and not s[j].isspace():
            j += 1

        # if we found some nonwhitespace characters
        if i != j:
            ret.append(s[i:j])
            i = j

    return ret


if __name__ == "__main__":
    # read and split each line of input
    for line in sys.stdin:
        for word in split(line.rstrip("\n")):
            print(word)
