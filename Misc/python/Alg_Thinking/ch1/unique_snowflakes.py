"""Unique Snowflakes (hash table solution)."""
import sys

SIZE = 100000


def code(snowflake):
    return sum(snowflake) % SIZE


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
    for bucket in snowflakes:
        for i in range(len(bucket)):
            for j in range(i + 1, len(bucket)):
                if are_identical(bucket[i], bucket[j]):
                    print("Twin snowflakes found.")
                    return
    print("No two snowflakes are alike.")


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    snowflakes = [[] for _ in range(SIZE)]
    pos = 1
    for _ in range(n):
        snow = [int(x) for x in data[pos:pos + 6]]
        pos += 6
        snowflakes[code(snow)].insert(0, snow)
    identify_identical(snowflakes)


if __name__ == "__main__":
    main()
