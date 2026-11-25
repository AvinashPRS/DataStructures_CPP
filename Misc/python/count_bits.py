"""Count the number of set bits (Brian Kernighan's trick)."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def count_num_bits_set(n):
    count = 0
    while n:
        n &= n - 1  # clears the lowest set bit
        count += 1
    return count


def main():
    if count_num_bits_set(0) != 0:
        handle_error()
    if count_num_bits_set(0xffffffff) != 32:
        handle_error()
    if count_num_bits_set(0x70ff00f) != 15:
        handle_error()
    print("Test passed")


if __name__ == "__main__":
    main()
