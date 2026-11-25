"""
Given an int 'n', find all primes between 1 and 'n' (Sieve of Eratosthenes).

Solution:
    Mark all numbers as prime candidates. Take the next unmarked number, it is a
    prime; mark all its multiples as non-prime.
    n/2 + n/3 + n/5 + ... + n/p ~ n * loglogn

    Space optimization: even numbers (other than 2) are not prime, so only odd
    numbers are stored. Index i represents the number 2*i + 3.

    TC: O(n * loglogn)
    SC: O(n)
"""


def find_all_primes(n):
    if n < 2:
        return []

    primes = [2]
    # index i represents number 2*i + 3, for all odd numbers 3..n
    size = (n - 1) // 2
    prime_candidates = [True] * size

    for i in range(size):
        if prime_candidates[i]:
            candidate = 2 * i + 3
            primes.append(candidate)
            # mark all odd multiples as non-prime, starting at candidate^2
            # candidate^2 is at index (candidate^2 - 3) / 2
            for j in range((candidate * candidate - 3) // 2, size, candidate):
                prime_candidates[j] = False

    return primes


if __name__ == "__main__":
    n = 115
    print(*find_all_primes(n))
