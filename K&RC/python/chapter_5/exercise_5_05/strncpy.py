"""Exercise 5-5: strncpy - copy at most n characters of t into s."""


def strncpy(s, t, n):
    """Overwrite the first n characters of s with those of t.

    Like the C version, if t is shorter than n, the copy stops at the end of
    t and the result ends there (the '\\0' terminator is copied).
    """
    copied = t[:n]
    if len(t) < n:
        return copied
    return copied + s[n:]


def main():
    s = "This is the first string"
    t = "Test is the second string, that is cool"
    nr_chars = 26

    print(strncpy(s, t, nr_chars))


if __name__ == "__main__":
    main()
