"""
Exercise 7-9. Functions like isupper can be implemented to save space or to
save time. Explore both possibilities.

In C the "time saving" versions are macros (no function-call overhead) and the
"space saving" versions wrap an if-statement around the library call. Python
has no macros, so they are shown here as small helper functions/lambdas.
"""
import sys

ISUPPER = lambda c: 1 if "A" <= c <= "Z" else 0                 # saves time  # noqa: E731
TOLOWER = lambda c: chr(ord(c) + ord("a") - ord("A"))           # saves time  # noqa: E731


def IFUPPER_TOLOWER(c):        # saves space
    return c.lower() if c.isupper() else c


def IF_UPPER_TOLOWER(c):       # saves time and space
    return TOLOWER(c) if ISUPPER(c) else c


def IF_UPPER(c, a):            # saves time and space
    return a if ISUPPER(c) else c


def main():
    sys.stdout.write("Enter an upper case character: ")
    sys.stdout.flush()
    c = sys.stdin.read(1) or "\n"

    if ISUPPER(c):
        c = c.lower()
    print(c)

    c = IFUPPER_TOLOWER(c)
    print(c)

    c = IF_UPPER_TOLOWER(c)
    print(c)

    print(IF_UPPER(c, TOLOWER(c)))


if __name__ == "__main__":
    main()
