"""
Problem:
    Given a number in base 'b1', convert the number to base 'b2'
    2 <= b1, b2 <= 16
    For numbers >= 10, use A for 10, B, ... F for 15

Input:
    num: (string) num in b1 for conversion
    b1: base 1
    b2: base 2

Output:
    number in base b2

For this first we will convert the number to base 10. After that convert it to b2.
TC: O( n * log_b2(b1) ) +  O(n), n = no. of characters in string num.
"""


def convert_to_decimal(num, base):
    """
    Converts a base b1 number to base 10.
    To change to base 10, we multiply the number with its base values raised
    to the power of digit position
    """
    num_10 = 0
    # check if negative
    negative = num[0] == "-"

    for c in num[1 if negative else 0:]:
        # multiply by base value
        num_10 *= base
        # in case the position is occupied by A, B.. F we convert it to
        # their values 10, 11,... 15
        if c.isdigit():
            num_10 += ord(c) - ord("0")
        else:
            num_10 += ord(c) - ord("A") + 10

    return -num_10 if negative else num_10


def convert_to_base(num, base):
    """Converts the number from decimal to given base"""
    if num == 0:
        return ""
    rem = num % base
    digit = chr(rem + ord("0")) if rem < 10 else chr(rem - 10 + ord("A"))
    return convert_to_base(num // base, base) + digit


def convert_bases_driver(num_b1, b1, b2):
    """Converts b1 --> b2"""
    # converts the number from given base to decimal
    num_10 = convert_to_decimal(num_b1, b1)
    # convert the number from decimal to given base
    return convert_to_base(num_10, b2)


if __name__ == "__main__":
    print(convert_to_decimal("1001", 2))
    print(convert_to_base(15, 2))
    print()

    print(convert_bases_driver("615", 7, 13))
