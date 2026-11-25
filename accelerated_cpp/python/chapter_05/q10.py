# Chapter 5, exercise 10: find all palindromes and the longest one.
import sys


def is_palindrome(s):
    return s == s[::-1]


def main():
    palindromes = []
    longest_word = ""
    for word in sys.stdin.read().split():
        if is_palindrome(word):
            palindromes.append(word)
            if len(word) > len(longest_word):
                longest_word = word

    if not palindromes:
        raise ValueError("no palindromes found")

    print("The palindrome(s) are: " + ", ".join(palindromes))
    print()
    print(f'The longest palindrome is "{longest_word}" with {len(longest_word)} letters.')


if __name__ == "__main__":
    main()
