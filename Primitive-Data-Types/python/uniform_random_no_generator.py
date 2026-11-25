"""
Problem:
    Given an unbiased function that generates 0 or 1, write a function that can generate
    a random number between the given range [a,b].

Input:
    Lower limit:a, Upper limit:b

Output:
    A number between [a,b]

NOTE: The original C++ file only contained the problem statement; this is an
implementation of it.
"""
import random


def zero_one_random():
    """The given unbiased function that generates 0 or 1"""
    return random.randint(0, 1)


def uniform_random(a, b):
    """
    Generates a uniform random number in [a, b] using only zero_one_random().
    There are (b - a + 1) outcomes. We build a random number bit by bit with
    enough bits to cover all outcomes, and retry if the result is out of range
    (rejection sampling), which keeps every outcome equally likely.
    TC: O(log(b - a + 1)) expected
    """
    number_of_outcomes = b - a + 1
    while True:
        result, i = 0, 0
        # generate a number with enough bits to represent all outcomes
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | zero_one_random()
            i += 1
        if result < number_of_outcomes:
            return result + a


if __name__ == "__main__":
    counts = {}
    for _ in range(6000):
        r = uniform_random(1, 6)
        counts[r] = counts.get(r, 0) + 1
    print(sorted(counts.items()))
