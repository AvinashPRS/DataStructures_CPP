import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def write_bit(x, bit_value, pos):
    """writes the bit_value (0/1) into position pos in x and returns the result"""
    mask = 1 << pos
    if bit_value:
        x = x | mask
    else:
        x = x & ~mask
    return x


def swap_bits(x, pos1, pos2):
    """
    x: integer in which the bits should be swapped
    pos1: position of first bit to be swapped
    pos2: position of the second bit to be swapped
    """
    # get the bits at position pos1 and pos2
    bit1 = (x >> pos1) & 1
    bit2 = (x >> pos2) & 1

    # swap the bits if the bits are different
    if bit1 != bit2:
        x = write_bit(x, bit1, pos2)
        x = write_bit(x, bit2, pos1)

    return x


def test(x, pos1, pos2, expected_result):
    result = swap_bits(x, pos1, pos2)

    print(f"Swapping bit {pos1} and bit {pos2} on 0x{x:x} = 0x{result:x}")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test(0xB, 1, 2, 0xD)
    test(0xB, 1, 0, 0xB)

    print("Test passed")
