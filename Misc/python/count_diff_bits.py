"""Number of bit positions in which two integers differ."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def count_different_bits(a, b):
    # positions where a and b differ are 1 in a ^ b; count those 1's
    c = a ^ b
    count = 0
    while c != 0:
        count += 1
        c &= c - 1
    return count


def main():
    if count_different_bits(0xF0F, 0x0F0) != 12:
        handle_error()
    if count_different_bits(4, 5) != 1:
        handle_error()
    print("Test passed")


if __name__ == "__main__":
    main()
