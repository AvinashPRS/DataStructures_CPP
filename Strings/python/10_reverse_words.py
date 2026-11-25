"""Reverse the order of words in a string, e.g. "Hello how" -> "how Hello"."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def reverse_string(chars, low, high):
    """
    Helper function which reverses a list of characters between indexes low and high
    """
    while low < high:
        chars[low], chars[high] = chars[high], chars[low]
        low += 1
        high -= 1


def is_alphabet(c):
    """Helper function which checks if a character is an alphabet (a-zA-Z)"""
    return ("A" <= c <= "Z") or ("a" <= c <= "z")


def reverse_words(chars):
    """
    Main function to reverse the words in a string
    chars: list of characters in which the words have to be reversed (in place)
    """
    length = len(chars)
    if length < 2:
        return

    # Reverse the entire string
    reverse_string(chars, 0, length - 1)

    # Reverse the individual words in the string
    pos = 0
    while pos < length:
        if is_alphabet(chars[pos]):
            low = pos
            while pos < length and is_alphabet(chars[pos]):
                pos += 1
            high = pos - 1
            reverse_string(chars, low, high)
        else:
            pos += 1


def reverse_words_pythonic(s):
    """Idiomatic alternative: reverse the whole string, then each word back."""
    return " ".join(word[::-1] for word in s[::-1].split(" "))


def test(str1, expected_result):
    print(f"{str1} ", end="")

    chars = list(str1)
    reverse_words(chars)
    result = "".join(chars)

    print(f"=>  {result}")

    if result != expected_result or reverse_words_pythonic(str1) != expected_result:
        handle_error()


if __name__ == "__main__":
    test("", "")
    test("a", "a")
    test("Hello how are you", "you are how Hello")

    print("Test passed")
