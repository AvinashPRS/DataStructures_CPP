"""Print all words corresponding to a telephone number."""

# digit 2 corresponds to ABC, 3 corresponds to DEF and so on
KEYPAD = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


def keypad_string_gen(digits, keypad, buf, pos):
    """Helper function for printing the words corresponding to the telephone number"""
    if pos == len(digits):
        # We have processed all the digits. So print the word and
        # terminate the recursion
        print("".join(buf))
        return

    cur_digit = digits[pos]

    # Guard against out-of-bounds digit input (e.g. negative numbers or > 9)
    if cur_digit < 0 or cur_digit > 9:
        return

    key_string = keypad[cur_digit]

    # If the mapped keypad string is empty, use a space as a filler so the
    # branch does not die completely
    if not key_string:
        buf[pos] = " "
        keypad_string_gen(digits, keypad, buf, pos + 1)
        return

    # Cycle through all the characters in the key_string
    for c in key_string:
        buf[pos] = c
        keypad_string_gen(digits, keypad, buf, pos + 1)


def telephone_digits_to_string(digits):
    """Main function for printing the words corresponding to the telephone number"""
    if len(digits) <= 0:
        print()
        return

    # Temporary buffer for storing the words corresponding to the digits
    buf = [""] * len(digits)
    keypad_string_gen(digits, KEYPAD, buf, 0)


if __name__ == "__main__":
    digits = [4, 2, 1, 1, 8, 9, 2, 5, 0, 8]
    telephone_digits_to_string(digits)

    print("Test passed")
