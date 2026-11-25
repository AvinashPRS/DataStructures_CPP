"""
Exercise 2-3. Write a function htoi(s), which converts a string of
hexadecimal digits (including an optional 0x or 0X) into its equivalent
integer value. The allowable digits are 0 through 9, a through f, and A
through F.
"""
import sys


def htoi(s):
    i = 0
    # detect optional 0x or 0X prefix
    if len(s) > 2 and s[0] == "0" and s[1].lower() == "x":
        i = 2
    int_value = 0
    for ch in s[i:]:
        c = ch.lower()
        if c.isdigit():
            hex_digit = ord(c) - ord("0")
        elif "a" <= c <= "f":
            hex_digit = ord(c) - ord("a") + 10
        else:
            return -1  # invalid input
        int_value = 16 * int_value + hex_digit
    return int_value


def main():
    s = input("Enter a hexadecimal string: ").split()[0]
    result = htoi(s)
    if result < 0:
        sys.exit(1)  # not a hexadecimal number
    print(result)


if __name__ == "__main__":
    main()
