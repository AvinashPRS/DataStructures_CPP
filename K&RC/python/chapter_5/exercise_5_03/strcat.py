"""Exercise 5-3: strcat(s, t) copies the string t to the end of s.

Python strings are immutable, so a list of characters is used to mimic the
pointer based C version.
"""


def strcat_ptr(s, t):
    """Append the characters of t to the list s (in place)."""
    # Find the end of s
    i = len(s)
    # Copy t to the end of s
    for ch in t:
        s.insert(i, ch)
        i += 1


def main():
    s = list("This is the first string")
    t = ", this second string!"

    strcat_ptr(s, t)

    print("".join(s))


if __name__ == "__main__":
    main()
