"""Convert a string to an integer (atoi)."""
import sys


def handle_error():
    print("Error occured ")
    sys.exit(1)


def function_atoi(s):
    """
    s: string to be converted to an integer
    Returns: integer value of the string
    """
    if not s:
        return 0

    val = 0
    is_negative = False
    i = 0
    if s[0] == "-":
        is_negative = True
        i += 1

    while i < len(s):
        if "0" <= s[i] <= "9":
            val = (val * 10) + (ord(s[i]) - ord("0"))  # convert char to int
        else:
            break
        i += 1

    if is_negative:
        val = -val

    return val


def test(str1, expected_result):
    result = function_atoi(str1)

    print(f"{str1} => {result}")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("-47", -47)
    test("987", 987)
    test("", 0)

    print("Test passed ")
