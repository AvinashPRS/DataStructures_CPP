"""
Given 'n', find the nth fibonacci number.

Solution:
    For each term we check if the previous term has been found or not; if not,
    find it and cache it, so each computation is done only once.

    TC: O(n)
    SC: O(n)
"""

_cache = {}


def nth_fibonacci_number(n):
    """finds the nth fibonacci number"""
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # if the cache has the value, return it
    if n in _cache:
        return _cache[n]

    _cache[n] = nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)
    return _cache[n]


if __name__ == "__main__":
    for n in range(6):
        print(nth_fibonacci_number(n))
