"""Remove duplicate characters from a string, keeping the first occurrence."""
import sys

MAX_NUM_CHARACTERS = 256


def handle_error():
    print("Test failed")
    sys.exit(1)


def remove_duplicates(chars):
    """
    chars: list of characters from which duplicate characters should be removed.
    The list is modified in place (Python strings are immutable).
    """
    if chars is None or len(chars) < 2:
        return

    was_char_observed = [False] * MAX_NUM_CHARACTERS

    was_char_observed[ord(chars[0])] = True
    fill_pos = 1
    for i in range(1, len(chars)):
        c = chars[i]

        # Only if current character was not observed so far, add the
        # current character to fill position and advance fill position
        if not was_char_observed[ord(c)]:
            chars[fill_pos] = c
            fill_pos += 1
        was_char_observed[ord(c)] = True

    # Truncate the list at fill position (equivalent of inserting '\0')
    del chars[fill_pos:]


def test(str1, expected_result):
    print(f"{str1} ", end="")

    chars = list(str1)
    remove_duplicates(chars)
    result = "".join(chars)

    print(f"=>  {result}")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("", "")
    test("a", "a")
    test("1aaaaaa2bbbaaaaa3cccccaaaabbb", "1a2b3c")

    print("Test passed")
