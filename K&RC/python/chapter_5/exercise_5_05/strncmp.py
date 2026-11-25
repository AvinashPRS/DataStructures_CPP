"""Exercise 5-5: strncmp - compare at most n characters of s and t.

Returns <0 if s<t, 0 if s==t, >0 if s>t.
"""


def strncmp(s, t, n):
    for i in range(n):
        cs = ord(s[i]) if i < len(s) else 0
        ct = ord(t[i]) if i < len(t) else 0
        if cs != ct:
            return cs - ct
        if cs == 0:
            return 0
    return 0


def main():
    s = "This is the first string"
    t = "This is the second string"
    nr_chars = 13

    is_equal = strncmp(s, t, nr_chars)

    if is_equal == 0:
        print("String s is equal with string t.")
    elif is_equal > 0:
        print("String s contains more chars than string t.")
    else:
        print("String s contains less chars than string t.")


if __name__ == "__main__":
    main()
