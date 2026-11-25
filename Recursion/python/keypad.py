"""
Print all letter combinations a phone-keypad digit string can represent.
"""

# Keypad mapping from 0 to 9
MAPPING = [
    "",      # 0
    "",      # 1
    "abc",   # 2
    "def",   # 3
    "ghi",   # 4
    "jkl",   # 5
    "mno",   # 6
    "pqrs",  # 7
    "tuv",   # 8
    "wxyz",  # 9
]


def solve(digits, output, index, mapping):
    """Recursive helper function."""
    # Base case: if index reaches the end of digits string, print the result
    if index == len(digits):
        print(output, end=" ")
        return

    # Get the characters corresponding to the current digit
    value = mapping[int(digits[index])]

    # Traverse all characters for this digit and make recursive calls
    for ch in value:
        solve(digits, output + ch, index + 1, mapping)


def print_keypad_combinations(digits):
    """Print all the key combinations."""
    if not digits:
        return
    solve(digits, "", 0, MAPPING)


if __name__ == "__main__":
    digits = "23"
    print(f"Combinations for {digits}: ", end="")
    print_keypad_combinations(digits)
    print()
