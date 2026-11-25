"""
Random number helpers built on a raw integer generator, mirroring the C version:
- unbiased uniform integers via rejection sampling
- Gaussian numbers via the Box-Muller transform

(In real Python code you would just use random.randint and random.gauss.)
"""
import math
import random
import time

RAND_MAX = 2147483647


def rand():
    """Equivalent of C's rand(): integer in [0, RAND_MAX]."""
    return random.randint(0, RAND_MAX)


def uniform_int_distribution_rand(low, high):
    """Generates an UNBIASED uniform integer in the inclusive range [low, high]."""
    # 1. Total number of items in the target range
    rng = high - low + 1

    # 2. Rejection threshold to eliminate modulo bias:
    #    the highest multiple of 'rng' that fits within RAND_MAX
    limit = RAND_MAX - (RAND_MAX % rng)

    while True:
        random_val = rand()
        if random_val < limit:  # Reject and re-roll if in the biased remainder zone
            break

    # 3. Map to the target range
    return low + random_val % rng


# Box-Muller produces two values at a time; cache the spare one between calls
_has_spare = False
_spare = 0.0


def generate_gaussian(mean, std_dev):
    """Generates random numbers following a normal (Gaussian) distribution."""
    global _has_spare, _spare

    # If we have a cached number from the previous transformation, return it
    if _has_spare:
        _has_spare = False
        return mean + std_dev * _spare

    # Two uniform random variables in (0, 1); ensure u1 is never 0 to avoid log(0)
    while True:
        u1 = rand() / RAND_MAX
        u2 = rand() / RAND_MAX
        if u1 > 0.0:
            break

    # Core Box-Muller transformation
    radius = math.sqrt(-2.0 * math.log(u1))
    theta = 2.0 * math.pi * u2

    # The transform yields two independent Gaussian numbers
    v1 = radius * math.cos(theta)
    v2 = radius * math.sin(theta)

    # Cache v2 for the next call
    _spare = v2
    _has_spare = True

    return mean + std_dev * v1


if __name__ == "__main__":
    # Seed once with the current time (like srand(time(NULL)))
    random.seed(time.time())

    low_bound, high_bound = 1, 6
    print("Simulating 10 unbiased dice rolls using rand():")
    print(" ".join(str(uniform_int_distribution_rand(low_bound, high_bound)) for _ in range(10)))

    print("Generating 10 Gaussian random numbers (Mean = 0, StdDev = 1):")
    for _ in range(10):
        print(f"{generate_gaussian(0.0, 1.0):f}")
