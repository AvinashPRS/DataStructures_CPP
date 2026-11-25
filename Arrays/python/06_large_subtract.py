"""
Subtract two large numbers whose digits are stored in arrays.

Solution:
    Keep the larger number in num1 (swap if needed and mark result negative).
    Subtract digit by digit from the least significant end, handling the borrow.

    TC: O(n), n = number of digits of the larger number
    SC: O(n)
"""
import random

MAX_NUM_TESTS = 10
MAX_VALUE = 10000


def convert_num_to_array(num):
    if num == 0:
        return [0]
    return [int(d) for d in str(num)]


def convert_array_to_num(a):
    num = 0
    for digit in a:
        num = num * 10 + digit
    return num


def is_smaller(num1, num2):
    """Returns True if num1 < num2 (both are digit arrays without leading zeros)."""
    if len(num1) != len(num2):
        return len(num1) < len(num2)
    for d1, d2 in zip(num1, num2):
        if d1 != d2:
            return d1 < d2
    return False


def large_subtract(num1, num2):
    """
    num1, num2: lists of digits (numeric values, most significant first)
    Returns (result digits, is_negative) for num1 - num2
    """
    is_negative = False
    if is_smaller(num1, num2):
        num1, num2 = num2, num1
        is_negative = True

    result = [0] * len(num1)
    pos1, pos2 = len(num1) - 1, len(num2) - 1
    borrow = 0

    # Subtract all the digits in num2
    while pos2 >= 0:
        difference = num1[pos1] - num2[pos2] - borrow
        if difference < 0:
            difference += 10
            borrow = 1
        else:
            borrow = 0
        result[pos1] = difference
        pos1 -= 1
        pos2 -= 1

    # Process any digits left over in num1
    while pos1 >= 0:
        difference = num1[pos1] - borrow
        if difference < 0:
            difference += 10
            borrow = 1
        else:
            borrow = 0
        result[pos1] = difference
        pos1 -= 1

    return result, is_negative


def digits_str(a):
    return "".join(map(str, a))


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        val1 = random.randrange(MAX_VALUE)
        val2 = random.randrange(MAX_VALUE)
        num1 = convert_num_to_array(val1)
        num2 = convert_num_to_array(val2)

        result, is_negative = large_subtract(num1, num2)
        print(f"{digits_str(num1)} - {digits_str(num2)} = {'-' if is_negative else ''}{digits_str(result)}")

        val3 = convert_array_to_num(result)
        if is_negative:
            val3 = -val3
        assert val3 == val1 - val2, "Error occured"

    print("Test passed")
