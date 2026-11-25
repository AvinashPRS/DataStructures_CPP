"""
Problem:
    Given a string, check if it is palindromic or not

Input:
    s = string

Output:
    bool

TC: O(n), n= no. of chars
"""


def is_palindrome(s):
    """Checks if a string is a palindrome or not"""
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    # also includes the case when the string is empty
    return True


if __name__ == "__main__":
    for s in ["aabscaa", " ", "a", "aabaa", "aa", ""]:
        print(int(is_palindrome(s)))
