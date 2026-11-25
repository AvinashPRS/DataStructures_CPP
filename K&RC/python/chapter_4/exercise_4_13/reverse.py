"""Exercise 4-13: recursive version of reverse(s)."""


def reverse(chars, i=0, j=None):
    """Reverse a list of characters in place, recursively."""
    if j is None:
        j = len(chars) - 1
    if i >= j:
        return
    chars[i], chars[j] = chars[j], chars[i]
    reverse(chars, i + 1, j - 1)


def main():
    s = list("This is just a string")

    print("".join(s))
    reverse(s)
    print("".join(s))


if __name__ == "__main__":
    main()

# NOTE: In C, static variables are handy in recursive functions; in Python
# extra (default) parameters carry the state between calls instead.
