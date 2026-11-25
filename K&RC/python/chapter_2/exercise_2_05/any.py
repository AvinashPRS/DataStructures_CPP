"""Exercise 2-5: any(s1, s2) returns the first location in s1 where any char
from s2 occurs, or -1 if s1 contains no chars from s2."""


def any_(str1, str2):
    for i, c in enumerate(str1):
        if c in str2:
            return i
    return -1


def main():
    str1 = "xxxabcabc"
    str2 = "cbaa"

    print(any_(str1, str2), end="")


if __name__ == "__main__":
    main()

# NOTE: The C standard library (string.h) contains strpbrk which does this.
# "any" is a Python builtin, so the function is named any_ here.
