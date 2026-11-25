"""Exercise 5-6: atoi rewritten with "pointers" (indices in Python)."""


def atoi(s):
    i = 0
    pos = 0
    while pos < len(s) and "0" <= s[pos] <= "9":
        i = i * 10 + ord(s[pos]) - ord("0")
        pos += 1
    return i


def main():
    s = "12s3a"
    print("atoi: %d" % atoi(s), end="")


if __name__ == "__main__":
    main()
