"""Exercise 7-9: two versions of isupper, one saving space and one saving
time."""

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_upper_v1(c):
    return "A" <= c <= "Z"


def is_upper_v2(c):
    return c in UPPERCASE


def main():
    if is_upper_v1("c"):
        print("is_upper_v1: This letter is uppercase.")
    else:
        print("is_upper_v1: This letter is lowercase.")

    if is_upper_v2("c"):
        print("is_upper_v2: This letter is uppercase.")
    else:
        print("is_upper_v2: This letter is lowercase.")


if __name__ == "__main__":
    main()
