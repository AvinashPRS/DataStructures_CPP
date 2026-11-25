"""Replace every space in a string with "%20" (in place, filling from the rear)."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def replace_space(chars):
    """
    chars: list of characters in which space characters (' ') should be
        replaced with %20. The list is grown to accommodate the extra characters.
    """
    # Count the number of spaces
    num_spaces = chars.count(" ")
    length = len(chars)

    # Make room for the extra characters at the end
    chars.extend([""] * (2 * num_spaces))
    fill_pos = length + (2 * num_spaces) - 1

    # Keep copying characters from rear of original string to fill position
    i = length - 1
    while i >= 0:
        if chars[i] == " ":
            # If we get a space, then place "%20" at fill position
            chars[fill_pos] = "0"
            chars[fill_pos - 1] = "2"
            chars[fill_pos - 2] = "%"
            fill_pos -= 3
        else:
            # Copy the character to fill position
            chars[fill_pos] = chars[i]
            fill_pos -= 1
        i -= 1


def test(str1, expected_result):
    print(f"{str1} ", end="")

    chars = list(str1)
    replace_space(chars)
    result = "".join(chars)

    if result != expected_result:
        handle_error()

    print(f"=>  {result}")


if __name__ == "__main__":
    test("", "")
    test("a", "a")
    test(" Hello  how are you ", "%20Hello%20%20how%20are%20you%20")

    print("Test passed")
