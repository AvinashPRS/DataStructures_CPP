"""Print all words corresponding to a telephone number on a phone keypad."""

# digit 2 corresponds to ABC, 3 to DEF and so on
KEYPAD = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


def keypad_string_gen(digits, keypad, buf, pos):
    """
    digits: list of digits 0-9
    keypad: characters corresponding to each digit
    buf: word formed so far
    pos: current position in buf and digits
    """
    if pos == len(digits):
        # All digits processed: print the word
        print("".join(buf))
        return
    # Cycle through all characters of the current digit's key string
    for ch in keypad[digits[pos]]:
        buf[pos] = ch
        keypad_string_gen(digits, keypad, buf, pos + 1)


def telephone_digits_to_string(digits):
    buf = [""] * len(digits)
    keypad_string_gen(digits, KEYPAD, buf, 0)


def main():
    digits = [4, 2, 1, 1, 8, 9, 2, 5, 0, 8]
    telephone_digits_to_string(digits)
    print("Test passed")


if __name__ == "__main__":
    main()
