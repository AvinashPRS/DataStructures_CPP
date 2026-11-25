"""Exercise 4-12: recursive version of itoa."""


def int_to_array(n):
    if n < 0:
        return "-" + int_to_array(-n)
    if n < 10:
        return chr(n + ord("0"))
    return int_to_array(n // 10) + chr(n % 10 + ord("0"))


def main():
    n = -1234
    print(int_to_array(n))

    n = -7676
    print(int_to_array(n), end="")


if __name__ == "__main__":
    main()
