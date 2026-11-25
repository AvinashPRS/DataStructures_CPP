# Chapter 7, exercise 9: nrand that works for arguments larger than RAND_MAX.
# Several rand() draws are combined into one wider random number, which is
# then reduced with the same bucketing trick to keep the result uniform.
from grammar import RAND_MAX, rand


def nrand(n):
    if n <= 0:
        raise ValueError("Argument to nrand is out of range")

    # number of distinct values a combination of k rand() calls can produce
    span = RAND_MAX + 1
    draws = 1
    while span < n:
        span *= RAND_MAX + 1
        draws += 1

    bucket_size = span // n
    while True:
        value = 0
        for _ in range(draws):
            value = value * (RAND_MAX + 1) + rand()
        r = value // bucket_size
        if r < n:
            return r


def main():
    print(f"RAND_MAX is {RAND_MAX}")
    print("The results for n = 100000 are: " + " ".join(str(nrand(100000)) for _ in range(5)))
    print("The results for n = 100 are: " + " ".join(str(nrand(100)) for _ in range(5)))


if __name__ == "__main__":
    main()
