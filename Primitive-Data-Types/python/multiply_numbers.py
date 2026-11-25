"""
Problem:
    Multiply two non negative numbers only using bitwise operators

Input:
    x = 1st number
    y = 2nd number

Output:
    product of x and y
"""


def add(total, y):
    """Adds two numbers using bit operators"""
    new_sum, carry_in, carry_out, k = 0, 0, 0, 1
    temp_sum, temp_y = total, y

    while temp_sum or temp_y:
        # get the bits at kth position
        sum_k, y_k = total & k, y & k
        # check if a carry bit will be formed or not
        carry_out = (sum_k & y_k) | (sum_k & carry_in) | (y_k & carry_in)
        # set the bit at kth position
        new_sum = new_sum | (carry_in ^ sum_k ^ y_k)
        # update carry
        carry_in = carry_out << 1
        k <<= 1
        temp_sum >>= 1
        temp_y >>= 1
    return new_sum | carry_in


def multiply(x, y):
    """Multiplies two numbers using bit operators only"""
    total = 0
    # since this is for binary numbers, we have only 1
    # or 0. For multiplication with 1, we get the same
    # number otherwise 0
    # Here y is multiplied by x
    while x:
        if x & 1:
            total = add(total, y)
        # since y is added to the total and each time it is
        # shifted by 1 step in every level
        y = y << 1
        x = x >> 1
    return total


if __name__ == "__main__":
    x, y = 13, 9
    prod = multiply(x, y)
    print(prod)
