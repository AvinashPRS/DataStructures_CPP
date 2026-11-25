"""
Given a real number, find its real square root. Answer will be the largest number
whose square is at most equal to the given number.

Input: float
Output: float

Solution:
    There are two important points to note:
    1. if 0 <= num < 1 : then its square root will be > num. So we set the limits
       as: l = num and r = 1.0
    2. if num >= 1: then we can set limits as:
       l = 1.0 and r = num

    With these limits we can just use binary search for finding the square root.
    TC: O(logn)
"""
import sys
from enum import Enum


class Category(Enum):
    FRACTIONAL_ONLY = 0
    NON_FRACTIONAL_ONLY = 1


class State(Enum):
    SMALLER = 0
    EQUAL = 1
    LARGER = 2


EPSILON = sys.float_info.epsilon


def decide_category_of_real_num(num):
    """Decides the category to which the real number belongs."""
    if num < 1.0:
        return Category.FRACTIONAL_ONLY
    return Category.NON_FRACTIONAL_ONLY


def compare_numbers(a, b):
    """Compares two real numbers using a relative tolerance."""
    diff = (a - b) / b  # normalization
    # Epsilon is the diff between 1 and the next representable number.
    if diff < -EPSILON:  # a < b
        return State.SMALLER
    elif diff > EPSILON:  # a > b
        return State.LARGER
    return State.EQUAL  # a == b


def find_real_square_root(num):
    """Finds the square root of a non-negative real number."""
    if num == 0:
        return 0.0

    # First find the category of the number
    category = decide_category_of_real_num(num)

    # Set the limits based on the category
    if category == Category.FRACTIONAL_ONLY:
        left, right = num, 1.0
    else:
        left, right = 1.0, num

    # Now search for the root using binary search
    while compare_numbers(left, right) == State.SMALLER:
        # Find the middle value
        middle = left + (right - left) / 2
        sq = middle * middle

        state = compare_numbers(sq, num)
        if state == State.SMALLER:  # square is smaller, change lower bound
            left = middle
        elif state == State.EQUAL:  # square root is found
            return middle
        else:  # square is larger, change upper bound
            right = middle

    return left


if __name__ == "__main__":
    num = 2.0
    print(f"{find_real_square_root(num):g}")
