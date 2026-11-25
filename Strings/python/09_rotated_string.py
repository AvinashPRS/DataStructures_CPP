"""Check if two strings are rotations of each other."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def is_string_rotation(str1, str2):
    """
    str1 and str2 are the two strings which need to be checked
    Returns: True if the two strings are rotations of each other, False otherwise
    """
    if str1 is None or str2 is None:
        return False

    # If lengths of two strings are not equal, then they can't be rotations
    if len(str1) != len(str2):
        return False

    # If str2 is a substring of str1 + str1, then str2 is a rotation of str1
    str3 = str1 + str1
    return str2 in str3


def test(str1, str2, expected_result):
    result = is_string_rotation(str1, str2)

    print(f"{str1} and {str2} are ", end="")
    print("rotations of each other" if result else "NOT rotations of each other")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("ABCDE", "CDEAB", True)
    test("ABCDE", "EABCD", True)
    test("AAA", "BBB", False)

    print("Test passed ")
