"""Reverse the bits of a 32-bit integer using a byte lookup table."""
import random
import sys

MAX_NUM_TESTS = 1000
NUM_BYTES = 4  # sizeof(int)


def get_rand_byte():
    return random.randrange(256)


def handle_error():
    print("Error occured ")
    sys.exit(1)


def reverse_integer(input_value, reverse_table):
    """
    reverse_table[b] holds the bit-reverse of byte b
    (e.g. reverse_table[0x01] = 0x80).
    """
    result = 0
    for _ in range(NUM_BYTES):
        cur_byte_value = input_value & 0xFF  # least significant byte
        result = ((result << 8) | reverse_table[cur_byte_value]) & 0xFFFFFFFF
        input_value >>= 8
    return result


def normal_reverse_integer(value, size_in_bits=32):
    result = 0
    j = size_in_bits - 1
    for i in range(size_in_bits):
        if value & (1 << i):
            result |= 1 << j
        j -= 1
    return result


def normal_reverse_char(value):
    return normal_reverse_integer(value, 8)


def main():
    lookup_table = [normal_reverse_char(i) for i in range(256)]

    for _ in range(MAX_NUM_TESTS):
        rand_num = (get_rand_byte() << 24) | (get_rand_byte() << 16) | \
            (get_rand_byte() << 8) | get_rand_byte()
        if normal_reverse_integer(rand_num) != reverse_integer(rand_num, lookup_table):
            handle_error()

    if reverse_integer(0, lookup_table) != 0:
        handle_error()
    if reverse_integer(0xffffffff, lookup_table) != 0xffffffff:
        handle_error()

    print("Test passed")


if __name__ == "__main__":
    main()
