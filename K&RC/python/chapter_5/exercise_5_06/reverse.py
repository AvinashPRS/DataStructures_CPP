"""Exercise 5-6: reverse rewritten with pointers (two indices)."""


def reverse(chars):
    if not chars:
        return
    s, t = 0, len(chars) - 1
    while s < t:
        chars[s], chars[t] = chars[t], chars[s]
        s += 1
        t -= 1


def main():
    s = list("test")
    reverse(s)
    print("".join(s))


if __name__ == "__main__":
    main()
