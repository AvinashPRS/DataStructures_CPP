"""Exercise 3-1: binary search with only one test inside the loop."""
import time

MAXLEN = 10000
ITERATIONS = 100000


def init_vector(n):
    return list(range(n))


def print_vector(v):
    print("[ " + ", ".join(str(x) for x in v) + " ]")


def binsearch_kr(x, v, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if x < v[mid]:
            high = mid - 1
        elif x > v[mid]:
            low = mid + 1
        else:
            return mid
    return -1


def binsearch(x, v, n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if x < v[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if low > 0 and x == v[low - 1]:
        return low - 1
    return -1


_test_nr = 0


def test_binsearch(search, x, v, n):
    global _test_nr
    start = time.perf_counter()

    for _ in range(ITERATIONS):
        search(x, v, n)

    elapsed = time.perf_counter() - start
    print("test_%d: %.4f seconds" % (_test_nr, elapsed))
    _test_nr += 1


def main():
    v = init_vector(MAXLEN)
    x = -1

    test_binsearch(binsearch_kr, x, v, MAXLEN)
    test_binsearch(binsearch, x, v, MAXLEN)


if __name__ == "__main__":
    main()

# NOTE: Using one test inside the loop instead of two may slightly increase
# the speed of binsearch(), although the gain is small on modern machines.
