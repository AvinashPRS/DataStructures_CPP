"""Check if any permutation of a string is a palindrome."""
import sys

NUM_CHARACTERS = 256


def handle_error():
    print("Test failed")
    sys.exit(1)


def is_permutation_palindrome(str1):
    """Returns True if there is at least one permutation of str1 which is a
    palindrome, False otherwise"""
    count = [0] * NUM_CHARACTERS

    # Find out how many times a character appears in the string
    for c in str1:
        count[ord(c)] += 1

    num_odd_char = 0
    for i in range(NUM_CHARACTERS):
        if count[i] % 2 == 1:
            num_odd_char += 1

        # If there are 2 or more characters that appear odd number of
        # times then we can't form a palindrome with any permutation of
        # the string
        if num_odd_char >= 2:
            return False

    return True


def test(str1, expected_result):
    result = is_permutation_palindrome(str1)
    if result:
        print(f"Permutation of {str1} is a palindrome")
    else:
        print(f"Permutation of {str1} is NOT a palindrome")

    if result != expected_result:
        handle_error()


if __name__ == "__main__":
    test("elelv", True)  # palindrome is level
    test("ab", False)

    print("Test passed")
