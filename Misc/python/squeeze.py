"""
Exercise 2-4. Write an alternative version of squeeze(s1,s2) that deletes
each character in s1 that matches any character in the string s2.
"""


def squeeze(s1, s2):
    return "".join(c for c in s1 if c not in s2)


def main():
    string1 = "clean* *this- *str*-ing *** ---"
    string2 = "*-"
    print(squeeze(string1, string2))


if __name__ == "__main__":
    main()
