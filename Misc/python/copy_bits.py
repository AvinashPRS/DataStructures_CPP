"""Copy bits start_pos..end_pos of src into dest (32-bit unsigned)."""
import sys

NUM_BITS_IN_INT = 32
ALL_ONES = (1 << NUM_BITS_IN_INT) - 1


def handle_error():
    print("Error occured ")
    sys.exit(1)


def copy_bits(dest, src, end_pos, start_pos):
    """
    end_pos: most significant bit position up to where bits are copied
    start_pos: least significant bit position from where bits are copied
    Returns dest after copying the bits from src.
    """
    num_bits_to_copy = end_pos - start_pos + 1
    # Right shift to remove the excess 1's in the mask
    ones_mask = ALL_ONES >> (NUM_BITS_IN_INT - num_bits_to_copy)
    # ones_mask now contains 1's from start_pos to end_pos
    ones_mask = (ones_mask << start_pos) & ALL_ONES
    # zeroes_mask contains 0's from start_pos to end_pos
    zeroes_mask = ~ones_mask & ALL_ONES
    dest &= zeroes_mask      # clear the bits in destination
    src &= ones_mask         # retain only the bits to copy
    return dest | src


def main():
    # Copy bits of b into a from position 7 to position 4
    a = 0xABCDEF
    b = 0xBBBBAB
    if copy_bits(a, b, 7, 4) != 0xABCDAF:
        handle_error()
    print("Test passed")


if __name__ == "__main__":
    main()
