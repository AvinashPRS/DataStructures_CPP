"""
Recursively prints all permutations of a string by building
a new permutation string character by character.
"""


def print_permutations_recursive(s, permutation=""):
    # Base Case: When the remaining string is empty, we've formed a full permutation
    if not s:
        print(permutation)
        return

    # Branching: Try picking every available character to be the next in the permutation
    for i, curr_char in enumerate(s):
        # Form a new string excluding the character we just picked
        remaining_str = s[:i] + s[i + 1:]

        # Recurse with the reduced string and updated permutation path
        print_permutations_recursive(remaining_str, permutation + curr_char)


if __name__ == "__main__":
    # Kick off the recursion with an empty permutation prefix
    print_permutations_recursive("abc")
