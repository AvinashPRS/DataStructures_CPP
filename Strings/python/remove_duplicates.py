"""Remove duplicate characters from a string, keeping the first occurrence."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def remove_duplicates(str1):
    """str1: string from which duplicate characters should be removed"""
    seen = set()
    result = []
    for c in str1:
        # Only if current character was not observed so far, keep it
        if c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result)


def test(str1, expected_result):
    result = remove_duplicates(str1)
    print(f"{str1} => {result}")
    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    # Test 1: Empty string
    test("", "")
    # Test 2: Single character
    test("a", "a")
    # Test 3: Repeated characters
    test("1aaaaaa2bbbaaaaa3cccccaaaabbb", "1a2b3c")

    print("Test passed")
