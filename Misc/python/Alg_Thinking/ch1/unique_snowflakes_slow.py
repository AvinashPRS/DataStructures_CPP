"""Unique Snowflakes - too slow (compares all pairs of snowflakes)."""
import sys


def identical_right(snow1, snow2, start):
    for offset in range(6):
        if snow1[offset] != snow2[(start + offset) % 6]:
            return False
    return True


def identical_left(snow1, snow2, start):
    for offset in range(6):
        if snow1[offset] != snow2[(start - offset) % 6]:
            return False
    return True


def are_identical(snow1, snow2):
    for start in range(6):
        if identical_right(snow1, snow2, start):
            return True
        if identical_left(snow1, snow2, start):
            return True
    return False


def identify_identical(snowflakes):
    n = len(snowflakes)
    for i in range(n):
        for j in range(i + 1, n):
            if are_identical(snowflakes[i], snowflakes[j]):
                print("Twin snowflakes found.")
                return
    print("No two snowflakes are alike.")


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    snowflakes = [[int(x) for x in data[1 + 6 * i:7 + 6 * i]] for i in range(n)]
    identify_identical(snowflakes)


if __name__ == "__main__":
    main()
