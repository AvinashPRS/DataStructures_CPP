"""
Reverse a number without using extra space

Input: int
Output: reversed number (int)

TC: O(n), n: no. of digits in number
"""


def reverse_number(num):
    """Reverses the input number without extra space"""
    # handle the sign separately since Python's % and // floor towards -inf
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_num = 0

    while num:
        reversed_num *= 10
        # add the last digit
        reversed_num += num % 10
        # remove the last digit from the original num
        num //= 10

    return sign * reversed_num


if __name__ == "__main__":
    num = 123
    print(reverse_number(num))
