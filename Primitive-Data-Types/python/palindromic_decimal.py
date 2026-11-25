"""
Problem: Given a decimal number, check whether it is palindromic or not without
using extra space.
NOTE: By decimal, it means the number is in base 10 and not that it is a float or double
value. Also negative numbers are not palindromic because of sign.

Input: decimal num(int)
Output: bool

TC: O(n), n: no. of digits
"""
import math


def num_digits_of(num):
    """Number of digits in a non-negative number (0 has 1 digit)"""
    return 1 if num == 0 else math.floor(math.log10(num)) + 1


def is_palindromic1(num):
    """
    Checks if the number is palindromic or not.
    Instead of using an array for storing the number as a series of digits, we can directly access
    the first and last digit and check if they are same or not. Then we reduce the number by
    ignoring the previous first and last digits. If at any point the digits are different we return false
    """
    # check if the number is negative or not
    if num < 0:
        return False

    # find the number of digits in the number
    num_digits = num_digits_of(num)

    # highest place value, this will be used for getting the MSB
    place_val = 10 ** (num_digits - 1)

    for _ in range(num_digits // 2):
        # get the first digit
        first = (num // place_val) % 10

        # get the last digit
        last = num % 10

        # check if the digits differ or not
        if last != first:
            return False

        # remove the last digit
        num //= 10
        # decrease the place value. We divide it by 100 to account for the removal
        # of last digit also
        place_val //= 100

    return True


def is_palindromic2(num):
    """
    Checks if the number is palindromic or not without extra space.
    Here instead of using place value for accessing the MSD (Most significant digit), we straight
    away remove the digit in every iteration.
    """
    # check if the number is negative
    if num < 0:
        return False

    # find the number of digits
    num_digits = num_digits_of(num)

    # mask for getting the number excluding the MSD
    place_val = 10 ** (num_digits - 1)

    for _ in range(num_digits // 2):
        # check if the digits are same
        if num % 10 != num // place_val:
            return False

        # remove the first digit
        num %= place_val
        # remove the last digit
        num //= 10
        # reduce the place value
        place_val //= 100

    return True


if __name__ == "__main__":
    for n in [0, 7, 121, 1221, 123, 10, -121]:
        print(n, is_palindromic1(n), is_palindromic2(n))
