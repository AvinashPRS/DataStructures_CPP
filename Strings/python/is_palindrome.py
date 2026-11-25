"""
Read words from standard input; report the palindromes and the longest one.

Usage: echo "level noon hello racecar" | python3 is_palindrome.py
"""
import sys


def is_palindrome(s):
    """check string palindromicity"""
    return s == s[::-1]


def main():
    palindromes = []
    longest_word = ""
    max_length = 0

    # read all input
    for word in sys.stdin.read().split():
        if is_palindrome(word):
            palindromes.append(word)
            # update the longest word
            if len(word) > max_length:
                longest_word = word
                max_length = len(word)

    # check if there are any palindromes
    if not palindromes:
        raise ValueError("no palindromes found")

    print("The palindrome(s) are: " + ", ".join(palindromes))
    print()
    print(f'The longest palindrome is "{longest_word}" with {max_length} letters.')


if __name__ == "__main__":
    main()
