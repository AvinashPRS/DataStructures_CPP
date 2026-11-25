"""Run length encoding of a string, e.g. "aaabb" -> "a3b2"."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def run_length_encode(str1):
    """
    str1: input string (example: "aaabb")
    Returns: encoded string (example: "a3b2")
    """
    if str1 is None:
        return None

    result = []
    pos = 0
    n = len(str1)
    while pos < n:
        c = str1[pos]

        # Count the number of consecutive occurences of character c
        count = 0
        while pos < n and str1[pos] == c:
            count += 1
            pos += 1

        # Store character c followed by its count in the output
        result.append(c)
        result.append(str(count))

    return "".join(result)


def test(str1, expected_result):
    result = run_length_encode(str1)
    print(f"{str1} => {result}")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("", "")
    test("a", "a1")
    test("abcde", "a1b1c1d1e1")
    test("aaabcccbba", "a3b1c3b2a1")

    print("Test passed")
