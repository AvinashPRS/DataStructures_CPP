"""
Objective:
Write a program to determine whether a given string is palindrome or not.

Input: malayalam
Output: yes

Input: algorithm
Output: no

A palindrome is a string that reads the same way in both the direction.
For e.g. racecar
"""


def is_palindrome(s):
    """
    Iterative Approach:

    Time Complexity: Theta(N)
    Space Complexity: Theta(1)
    """
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def is_palindrome_rec(s, start, end):
    """
    Recursive Approach

    Time Complexity: Theta(N)
    Space Complexity: Theta(N)
    """
    if start >= end:  # 0 or 1 char long string case
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome_rec(s, start + 1, end - 1)  # shrink now


if __name__ == "__main__":
    print("Program that determines whether a given string is palindrome or not!")
    # Converting to lower case to make it case insensitive
    s = input("Enter the string: ").strip().lower()

    if is_palindrome_rec(s, 0, len(s) - 1):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome")
