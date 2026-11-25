"""Exercise 3-5: itob(n, s, b) converts integer n into a base b string."""


def c_div(a, b):
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


def itoc(a):
    if a <= 9:
        return chr(a + ord("0"))
    return chr(a + ord("a") - 10)


def itob(n, b):
    sign = n
    s = []

    while True:
        s.append(itoc(abs(n) % b))
        n = c_div(n, b)
        if n == 0:
            break

    if b == 2:
        s.extend("b0")
    elif b == 16:
        s.extend("x0")

    if sign < 0:
        s.append("-")

    return "".join(reversed(s))


def main():
    n = -2
    print(itob(n, 16), end="")


if __name__ == "__main__":
    main()

# NOTE: Converting an integer to any base: take the remainder of the number
# divided by base, then divide the number by base. Reverse the result.
