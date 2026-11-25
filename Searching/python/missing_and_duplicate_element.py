"""
Given an array of 'n' ints whose values lie in [0, n-1]. One number has been repeated twice.
Find the duplicate number and the number of the range [0, n-1] missing from the array.

Input: list of int
Output: (missing, duplicate)

Solution:
    Take the XOR of [0, n-1] and of the array. Since XOR of same value is 0, and the
    array has all the values from [0, n-1] except for one, every number cancels and
    only the duplicate and missing numbers are left.
    i.e. final XOR result = missing XOR duplicate
    Since they are different, there must be some set bits in the XOR.
    We take any set bit and take XOR of all numbers in the array as well as in [0, n-1]
    with the bit set at that position.

    The XOR of these gives either duplicate or missing, since we don't know which of
    the two had the bit set at that position.

    To know which it is, we search for it in the array: if found it is the duplicate,
    else it is the missing number.

    TC: O(n)
"""
from collections import namedtuple

MissingAndDuplicate = namedtuple("MissingAndDuplicate", ["missing", "duplicate"])


def find_missing_and_duplicate_number(arr):
    """Finds the missing and duplicate numbers from the array."""
    arr_xor = 0
    range_xor = 0

    # First take XOR of both the range and array
    for i, a in enumerate(arr):
        arr_xor ^= a
        range_xor ^= i

    # Now get missing XOR duplicate value
    miss_xor_dup = arr_xor ^ range_xor

    # Now get the lowest set bit and create a mask of it
    set_kth_bit_mask = miss_xor_dup & ~(miss_xor_dup - 1)

    # Take XOR of all those with set bit as that of set_kth_bit_mask
    xor_kth_bit_arr = 0
    xor_kth_bit_range = 0
    for i, a in enumerate(arr):
        # If the current number in array has a set bit at kth position
        if a & set_kth_bit_mask:
            xor_kth_bit_arr ^= a
        # If the current number in range has a set bit at kth position
        if i & set_kth_bit_mask:
            xor_kth_bit_range ^= i

    # This can be either duplicate or missing number
    unknown_num = xor_kth_bit_range ^ xor_kth_bit_arr

    # If this number is found in the array then it is the duplicate number,
    # otherwise it is the missing number
    if unknown_num not in arr:
        return MissingAndDuplicate(unknown_num, miss_xor_dup ^ unknown_num)
    return MissingAndDuplicate(miss_xor_dup ^ unknown_num, unknown_num)


if __name__ == "__main__":
    # Given range: 0-10, with 4 missing
    arr = [0, 1, 2, 3, 5, 5, 6, 7, 8, 9, 10]

    miss_dup = find_missing_and_duplicate_number(arr)
    print(f"Missing: {miss_dup.missing}\nDuplicate: {miss_dup.duplicate}")
