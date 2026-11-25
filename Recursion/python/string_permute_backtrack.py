"""
Generates all permutations of a string in-place using swap-based backtracking.
(Python strings are immutable, so the string is held as a list of characters.)
"""


def print_permutations_in_place(chars, index=0):
    """
    :param chars: the original string as a list of characters (mutated in place)
    :param index: the current starting index for swapping
    """
    # Base Case: If we reach the end of the string, we found a full permutation
    if index >= len(chars):
        print("".join(chars))
        return

    for i in range(index, len(chars)):
        # Step 1: Swap the current index character with the i-th character
        chars[index], chars[i] = chars[i], chars[index]

        # Step 2: Recurse for the remaining substring
        print_permutations_in_place(chars, index + 1)

        # Step 3: Backtrack (Undo the swap to restore the original string state)
        chars[index], chars[i] = chars[i], chars[index]


if __name__ == "__main__":
    # Start backtracking from index 0
    print_permutations_in_place(list("abc"))

    # For the non-backtracking recursive implementation, see print_string_permutation.py
