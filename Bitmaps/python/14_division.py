import sys

MAX_NUMERATOR = 100
MAX_DENOMINATOR = 20
MAX_BIT_POS = 31  # (sizeof(int) * 8) - 1


def handle_error():
    print("Error occured ")
    sys.exit(1)


def integer_division(a, b):
    """
    a, b: a is an integer >= 0. b is an integer > 0
    Return value: (quotient, remainder) of a / b
    Raises ZeroDivisionError if b is 0
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")

    quotient = remainder = 0
    for i in range(MAX_BIT_POS, -1, -1):
        remainder = remainder << 1  # double the remainder

        # Find the value of the next bit in the dividend a.
        # In first iteration, we find value of the Most Significant Bit
        next_bit = 1 if a & (1 << i) else 0

        # Copy the value of the next bit into the least significant
        # bit of remainder
        if next_bit:
            remainder = remainder | 1

        # If the remainder is now greater than the divisor b,
        # then subtract the divisor b from the remainder and
        # set the appropriate quotient bit
        if remainder >= b:
            remainder = remainder - b
            quotient = quotient | (1 << i)

    return quotient, remainder


if __name__ == "__main__":
    for a in range(MAX_NUMERATOR):
        for b in range(1, MAX_DENOMINATOR):
            quotient, remainder = integer_division(a, b)

            print(f"({a} / {b}) => quotient = {quotient}, remainder = {remainder} ")

            if quotient != a // b:
                handle_error()

            if remainder != a % b:
                handle_error()

    print("Test passed ")
