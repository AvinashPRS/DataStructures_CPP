import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def count_num_bits_set(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


if __name__ == "__main__":
    if count_num_bits_set(0) != 0:
        handle_error()

    if count_num_bits_set(0xFFFFFFFF) != 32:
        handle_error()

    if count_num_bits_set(0x70FF00F) != 15:
        handle_error()

    print("Test passed")
