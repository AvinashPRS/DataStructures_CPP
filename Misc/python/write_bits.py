"""Swap two bits of an integer."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def write_bit(x, bit_value, pos):
    """Write bit_value (0/1) into position pos of x."""
    mask = 1 << pos
    return x | mask if bit_value else x & ~mask


def swap_bits(x, pos1, pos2):
    bit1 = (x >> pos1) & 1
    bit2 = (x >> pos2) & 1
    # swap only if the bits differ
    if bit1 != bit2:
        x = write_bit(x, bit1, pos2)
        x = write_bit(x, bit2, pos1)
    return x


def test(x, pos1, pos2, expected_result):
    result = swap_bits(x, pos1, pos2)
    print(f"Swapping bit {pos1} and bit {pos2} on 0x{x:x} = 0x{result:x}")
    if result != expected_result:
        handle_error()


def main():
    test(0xB, 1, 2, 0xD)
    test(0xB, 1, 0, 0xB)
    print("Test passed")


if __name__ == "__main__":
    main()
