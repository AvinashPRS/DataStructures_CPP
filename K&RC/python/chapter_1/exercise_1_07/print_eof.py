"""Exercise 1-7: print the value of EOF."""

# Python has no EOF constant; C's EOF is the integer -1. In Python, reading
# from a file at end-of-file returns an empty string ("").
EOF = -1


def main():
    print("EOF: %d" % EOF, end="")


if __name__ == "__main__":
    main()
