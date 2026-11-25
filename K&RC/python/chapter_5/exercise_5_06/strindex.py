"""Exercise 5-6: strindex rewritten with pointers."""


def strindex(s, t):
    for pos in range(len(s)):
        if s[pos:pos + len(t)] == t and t:
            return pos
    return -1


def main():
    s = "this is first string"
    t = "this"
    print(strindex(s, t), end="")


if __name__ == "__main__":
    main()
