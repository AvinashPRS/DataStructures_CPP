"""
Problem:
    Write functions that can convert a string encoded integer to an integer and vice versa

Input:
    s: string encoded integer
    num: int
Output:
    num: integer equivalent
    s: string equivalent
"""


def string_to_int(s):
    """Converts a string to integer. TC: O(n)"""
    if not s:
        return 0

    # check if the number is negative or not
    negative = s[0] == "-"
    num = 0

    for c in s[1 if negative else 0:]:
        # multiply by the base value for its digit position and add the digit
        num = num * 10 + (ord(c) - ord("0"))

    return -num if negative else num


def int_to_string(num):
    """Converts an integer to its string representation. TC: O(n)"""
    negative = num < 0
    # make the no. +ve for calculations
    if negative:
        num = -num

    digits = []
    while True:
        # take out the last digit
        digits.append(chr(ord("0") + num % 10))
        num //= 10
        if num == 0:
            break

    # add the negative sign if req
    if negative:
        digits.append("-")

    # reverse to make the number representation correct
    return "".join(reversed(digits))


if __name__ == "__main__":
    print(string_to_int(""))
    print(string_to_int("0"))
    print(string_to_int("-21"))
    print(string_to_int("2112"))
    print()
    print(int_to_string(0))
    print(int_to_string(111))
    print(int_to_string(-1212))
