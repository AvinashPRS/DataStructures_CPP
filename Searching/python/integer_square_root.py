"""Find the integer square root (floor of sqrt) of a non-negative integer."""


def find_integer_square_root(n):
    # Lower and upper limits
    left, right = 0, n

    while left <= right:
        # Middle number
        middle = left + (right - left) // 2
        # Square of current middle number
        sq_val = middle * middle

        # Return if its value is equal
        if sq_val == n:
            return middle
        # If the square is lesser than the target number, then increase the
        # lower limit
        elif sq_val < n:
            left = middle + 1
        # If the square is greater, all numbers after it are greater as well
        else:
            right = middle - 1

    # left - 1 is always the largest number whose square is lesser than n
    return left - 1


if __name__ == "__main__":
    num = 1
    print(find_integer_square_root(num))
