"""
Divide x / y without using the '/' operator.
"""

INT_MAX = 2**31 - 1
N_BITS = 32


def divide(x, y):
    divisor = y
    dividend = x
    quotient = 0

    # decide the sign
    negative = (x < 0) ^ (y < 0)
    divisor, dividend = abs(divisor), abs(dividend)

    # We start with the largest permissible multiple for the divisor
    # such that the divisor is still smaller than dividend,
    # then we add that bit to the quotient. The dividend is updated
    # with dividend = dividend - divisor*multiple
    # Then we again find the next largest multiple that when multiplied with divisor
    # gives a value closer to dividend. Continue doing this till we get 0
    for i in range(N_BITS - 1, -1, -1):
        # 2^i * divisor <= dividend
        if (divisor << i) <= dividend:
            dividend -= divisor << i  # dividend = dividend - divisor*2^i
            quotient |= 1 << i

    # add the sign if required
    quotient = -quotient if negative else quotient

    # check for overflow
    if quotient > INT_MAX:
        quotient = INT_MAX
    return quotient


if __name__ == "__main__":
    print(divide(10, 3))
    print(divide(7, -3))
    print(divide(-2**31, -1))
