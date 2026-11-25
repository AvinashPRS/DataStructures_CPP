"""Exercise 3-3: expand(s1, s2) expands shorthand notations like a-z in s1
into the equivalent complete list abc...xyz in s2.

Handled cases: a-z, a-b-c, a-c-h-v, 0-9, a-zA-Z, 0-9a-zA-Z, leading and
trailing '-' are taken literally.
"""
import sys


def expand(src):
    dest = []
    n = len(src)

    def at(k):
        return src[k] if k < n else "\0"

    i = 0
    while i < n:
        if at(i).isalnum() and at(i + 1) == "-" and at(i) < at(i + 2):
            while at(i).isalnum() and at(i + 1) == "-" and at(i) < at(i + 2):
                for code in range(ord(at(i)), ord(at(i + 2)) + 1):
                    ch = chr(code)
                    if (not dest or dest[-1] != ch) and ch.isalnum():
                        dest.append(ch)
                i += 2
            # Skip the last range end (already written)
            i += 1
        else:
            dest.append(src[i])
            i += 1

    return "".join(dest)


def main():
    sys.stdout.write(expand(sys.stdin.read()))


if __name__ == "__main__":
    main()
