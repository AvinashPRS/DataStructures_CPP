"""Convert a Roman numeral string into an integer."""
import sys

ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def handle_error():
    print("Error occured ")
    sys.exit(1)


def get_numeric_value(c):
    """Helper function that returns the numeric value of a Roman alphabet"""
    return ROMAN_VALUES.get(c, 0)


def roman_to_int(str1):
    """
    str1: valid input string with Roman alphabets
    Returns: integer equivalent of the Roman string
    """
    # Process the string from the rear
    i = len(str1) - 1
    if i < 0:
        return 0

    result = get_numeric_value(str1[i])
    i -= 1
    while i >= 0:
        cur_value = get_numeric_value(str1[i])
        next_value = get_numeric_value(str1[i + 1])

        if cur_value < next_value:
            result -= cur_value
        else:
            result += cur_value
        i -= 1

    return result


def test(str1, expected_result):
    result = roman_to_int(str1)

    print(f"{str1} => {result}")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("MMCX", 2110)
    test("MMXC", 2090)
    test("LIX", 59)
    test("LVIIII", 59)
    test("X", 10)
    test("", 0)

    print("Test passed ")
