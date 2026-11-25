"""Exercise 3-4: itoa that also handles the largest negative number."""


def c_div(a, b):
    """Integer division truncating toward zero, like C."""
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


def c_mod(a, b):
    return a - b * c_div(a, b)


def int_to_array(n):
    sign = n
    s = []

    while True:
        s.append(chr(abs(c_mod(n, 10)) + ord("0")))
        n = c_div(n, 10)
        if n == 0:
            break

    if sign < 0:
        s.append("-")

    return "".join(reversed(s))


def main():
    n = 785
    print(int_to_array(n))


if __name__ == "__main__":
    main()

# NOTE: In C, n = -n is not enough for the smallest negative number because it
# has no positive equivalent. Taking abs(n % 10) gives the correct digit.
