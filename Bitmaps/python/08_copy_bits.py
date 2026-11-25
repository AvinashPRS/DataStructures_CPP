import sys

NUM_BITS_IN_INT = 32
MASK32 = 0xFFFFFFFF


def handle_error():
    print("Error occured ")
    sys.exit(1)


def copy_bits(dest, src, end_pos, start_pos):
    """
    dest: destination integer into which the bits have to be copied
    src: source integer from which the bits have to be copied
    end_pos: Most Significant bit position upto where the bits should be copied
    start_pos: Least Significant bit position from where the bits should be copied
        end_pos should be >= start_pos
    Return value: result integer after copying bits from source to destination
    """
    num_bits_to_copy = end_pos - start_pos + 1
    ones_mask = MASK32  # all ones

    # Use the bit-wise right shift operator to remove the excess 1's in the mask
    ones_mask = ones_mask >> (NUM_BITS_IN_INT - num_bits_to_copy)

    # Left shift the 1's to the starting position. ones_mask will contain 1's
    # from start_pos to end_pos
    ones_mask = (ones_mask << start_pos) & MASK32

    # zeroes_mask will contain 0's from start_pos to end_pos
    zeroes_mask = ~ones_mask & MASK32

    # clear the bits in destination from start_pos to end_pos
    dest = dest & zeroes_mask

    # retain the bits in source from start_pos to end_pos and clear the
    # remaining bits
    src = src & ones_mask

    # copy the source bits into the destination
    return dest | src


if __name__ == "__main__":
    # Copy bits of b into a from position 7 to position 4
    a = 0xABCDEF
    b = 0xBBBBAB
    if copy_bits(a, b, 7, 4) != 0xABCDAF:
        handle_error()

    print("Test passed")
