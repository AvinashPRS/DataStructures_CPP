"""
Validate that a string of brackets {}, [], () is properly nested.
Any character other than a bracket makes the string invalid.

Solution:
    Push opening brackets on a stack. For a closing bracket, the top of the stack must be
    the matching opening bracket. At the end the stack must be empty.
    TC: O(n), SC: O(n)
"""
import sys

MATCHING = {"}": "{", "]": "[", ")": "("}


def handle_error():
    print("Test failed")
    sys.exit(1)


def validate_nesting(str1):
    s = []

    for c in str1:
        if c in "{[(":
            s.append(c)
        elif c in "}])":
            if not s:
                return 0
            if s[-1] != MATCHING[c]:
                return 0
            s.pop()
        else:
            return 0

    if s:
        return 0

    return 1


def test(str1, expected_result):
    result = validate_nesting(str1)

    if result:
        print(f'"{str1}" => is balanced ')
    else:
        print(f'"{str1}" => is NOT balanced ')

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    # Original test cases
    test("[{()}]", 1)
    test("[{]", 0)

    # Critical edge cases
    test("", 1)        # Empty string (should be balanced)
    test("(", 0)       # Single open bracket (unbalanced)
    test("]", 0)       # Single close bracket (unbalanced)
    test("([)]", 0)    # Correct types but interleaved incorrectly
    test("abc", 0)     # Non-bracket characters (should fail per current logic)

    print("\nAll tests passed safely!")
