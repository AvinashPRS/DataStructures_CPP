import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def count_different_bits(a, b):
    """
    a, b: the two input integers
    Return value: Number of bits that have different values in a and b
    """
    c = a ^ b
    count = 0

    # Since c = a xor b, the positions where a and b are different will
    # be set to 1 in c. So by counting the number of 1's in c, we will get the
    # number of bits that are different between a and b
    while c != 0:
        count += 1
        c = c & (c - 1)

    return count


if __name__ == "__main__":
    if count_different_bits(0xF0F, 0x0F0) != 12:
        handle_error()

    if count_different_bits(4, 5) != 1:
        handle_error()

    print("Test passed")
