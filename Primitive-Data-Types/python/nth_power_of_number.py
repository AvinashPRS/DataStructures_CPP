"""
Problem:
    Find the nth power of a number

Input:
    Real no. x, power n

Output:
    x raised to n
"""


def find_power(num, i):
    """
    Finds the power of the number.
    TC: O(logn), n=power
    The power can be broken down in terms of squares of smaller numbers
    """
    # base case
    if i == 0:
        return 1

    # int(i / 2) truncates towards zero like C++ integer division
    val = find_power(num, int(i / 2))

    # if the power is even
    if i % 2 == 0:
        return val * val
    # if the power is odd
    # if positive power
    if i > 0:
        return val * val * num
    # if negative power
    return val * val * 1.0 / num


def find_nth_power_rec(num, n):
    """Finds the nth power of a number recursively"""
    # when the number is zero
    if num == 0:
        return 0
    # base case when the power is zero
    if n == 0:
        return 1
    # when the exponent is negative
    if n == -1:
        return 1.0 / num
    # find the value by making further calls
    val = find_nth_power_rec(num, n >> 1)
    # if the last digit is 1, that means the exponent is formed by adding exponent 1, so multiply
    # by the number. Eg: 2^(101): 2^(10)*2^(10)*2^(1)
    if n & 1:
        return num * val * val
    return val * val


def find_power2_iter(x, n):
    """
    Finds the nth power of a number using the bit representation iteratively.
    TC: O(n), n=no. of bits
    """
    result = 1.0

    # if the power is negative
    if n < 0:
        x = 1.0 / x
        # make the power positive now that x has been made 1/x
        n = -n

    # till the power is not zero
    while n:
        # if the last digit is 1, that means the exponent is formed by adding exponent 1, so multiply
        # by the number. Eg: 2^(101): 2^(10)*2^(10)*2^(1)
        if n & 1:
            result = result * x
        # find the square of current number for the next iteration
        x = x * x
        # reduce the power by a factor of 2
        n >>= 1
    return result


if __name__ == "__main__":
    print(f"{find_power(2, -3):g}, {find_power2_iter(2, -3):g}")
    print(f"{find_nth_power_rec(2, 4):g}, {find_power2_iter(2, 4):g}")
    print(f"{find_nth_power_rec(2, -1):g}, {find_power2_iter(2, -1):g}")
    print(f"{find_nth_power_rec(2, -2):g}, {find_power2_iter(2, -2):g}")
    print(f"{find_nth_power_rec(3, 2):g}, {find_power2_iter(3, 2):g}")
    print(f"{find_nth_power_rec(3, 3):g}, {find_power2_iter(3, 3):g}")
    print(f"{find_nth_power_rec(3, -1):g}, {find_power2_iter(3, -1):g}")
