"""
Reverse a string recursively.
"""


def rev_string(s):
    # Base Case: Handle both empty strings and the end of the recursion safely
    if not s:
        return s

    curr_char = s[0]

    # Reverse the substring from index 1 to the end
    next_string = rev_string(s[1:])

    # Append the current character to the end of the reversed remaining string
    return next_string + curr_char


def rev_string_in_place(chars, start, end):
    """
    Optimized: operates on a list of characters in place to avoid creating copies
    (Python strings are immutable).
    """
    # Base case: Pointers have met or crossed
    if start >= end:
        return

    # Swap the characters at the boundary positions
    chars[start], chars[end] = chars[end], chars[start]

    # Recursive step: Move boundaries inward
    rev_string_in_place(chars, start + 1, end - 1)


if __name__ == "__main__":
    s = "avinash"
    print(f"Reversed string: {rev_string(s)}")  # Output: hsaniva

    chars = list(s)
    rev_string_in_place(chars, 0, len(chars) - 1)
    print(f"Reversed string (in place): {''.join(chars)}")
