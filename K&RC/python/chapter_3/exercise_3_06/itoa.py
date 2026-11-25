"""Exercise 3-6: itoa with a minimum field width (padded with blanks)."""


def c_div(a, b):
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


def c_mod(a, b):
    return a - b * c_div(a, b)


def ilen(a):
    i = 0
    while True:
        i += 1
        a = c_div(a, 10)
        if a == 0:
            break
    return i


def int_to_array(n, padding):
    sign = n
    s = []

    while True:
        s.append(chr(abs(c_mod(n, 10)) + ord("0")))
        n = c_div(n, 10)
        if n == 0:
            break

    if sign < 0:
        s.append("-")

    length = ilen(sign)
    while length < padding:
        s.append(" ")
        padding -= 1

    return "".join(reversed(s))


def main():
    n = 1995
    print(int_to_array(n, 6))


if __name__ == "__main__":
    main()
