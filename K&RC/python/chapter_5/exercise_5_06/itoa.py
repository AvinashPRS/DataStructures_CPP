"""Exercise 5-6: itoa rewritten with pointers."""


def reverse(chars):
    i, j = 0, len(chars) - 1
    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1


def itoa(n):
    s = []
    while n:
        s.append(chr(n % 10 + ord("0")))
        n //= 10
    reverse(s)
    return "".join(s)


def main():
    i = 1234
    print("itoa: %s" % itoa(i))


if __name__ == "__main__":
    main()
