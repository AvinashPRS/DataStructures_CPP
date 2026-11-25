"""Exercise 2-4: squeeze(s1, s2) deletes each char in s1 that matches any
char in s2."""


def squeeze(str1, str2):
    for k in str2:
        str1 = "".join(c for c in str1 if c != k)
    return str1


def main():
    str1 = "abcdefg"
    str2 = "abcd"

    print(squeeze(str1, str2), end="")


if __name__ == "__main__":
    main()
