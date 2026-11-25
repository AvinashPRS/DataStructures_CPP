import random
import sys

MAX_NUM_TESTS = 1000
NUM_BYTES = 4  # sizeof(int)
MASK32 = 0xFFFFFFFF


def get_rand_byte():
    return random.randint(0, 255)


def handle_error():
    print("Error occured ")
    sys.exit(1)


def reverse_integer(input_value, reverse_table):
    """
    input_value: the integer that has to be reversed
    reverse_table: lookup table that has the reversed values for every byte.
        Example - reverse_table[0x1] = 0x80, since reverse of 00000001 is 10000000
    Return value: integer that is the reverse of the input integer
    """
    result = 0
    for _ in range(NUM_BYTES):
        # Get the least significant byte from the input
        cur_byte_value = input_value & 0xFF

        # Left shift the result by 8 and append the reverse of the
        # least significant byte of input
        result = ((result << 8) | reverse_table[cur_byte_value]) & MASK32

        # Right shift out the least significant byte from the input
        input_value >>= 8
    return result


def normal_reverse(value, size_in_bits):
    result = 0
    j = size_in_bits - 1
    for i in range(size_in_bits):
        if value & (1 << i):
            result |= 1 << j
        j -= 1
    return result


def normal_reverse_integer(value):
    return normal_reverse(value, NUM_BYTES * 8)


def normal_reverse_char(value):
    return normal_reverse(value, 8)


if __name__ == "__main__":
    lookup_table = [normal_reverse_char(i) for i in range(256)]

    for _ in range(MAX_NUM_TESTS):
        rand_num = (get_rand_byte() << 24) | (get_rand_byte() << 16) | \
                   (get_rand_byte() << 8) | get_rand_byte()

        normal_result = normal_reverse_integer(rand_num)
        lookup_result = reverse_integer(rand_num, lookup_table)

        if normal_result != lookup_result:
            handle_error()

    rand_num = 0
    if rand_num != reverse_integer(rand_num, lookup_table):
        handle_error()

    rand_num = 0xFFFFFFFF
    if rand_num != reverse_integer(rand_num, lookup_table):
        handle_error()

    print("Test passed")
