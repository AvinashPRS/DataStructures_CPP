"""Exercise 4-14: swap(t, x, y) macro that interchanges two arguments.

Python has no preprocessor macros; tuple unpacking swaps values directly.
"""


def main():
    x = 2
    y = 3

    print("x: %d, y: %d" % (x, y))

    x, y = y, x
    print("x: %d, y: %d" % (x, y))


if __name__ == "__main__":
    main()
