"""
Exercise 2-5. Write the function any(s1, s2), which returns the first
location in a string s1 where any character from the string s2 occurs, or -1
if s1 contains no characters from s2. (The standard library function strpbrk
does the same job but returns a pointer to the location.)
"""


def any_char(s1, s2):
    for i, c in enumerate(s1):
        if c in s2:
            return i
    return -1


def main():
    string1 = "search me please"
    string2 = "wmp"
    print(any_char(string1, string2))


if __name__ == "__main__":
    main()
