"""
Given a string, find whether it can be made a palindrome by rearranging its characters.
Input: string
Output: bool

Solution:
    A string can be rearranged into a palindrome if every character occurs an even number
    of times, except at most one character (the middle one for odd lengths).
    Build a hash table of char -> frequency and count the odd frequencies.

    TC: O(n), n: no. of chars
    SC: O(m), m: unique characters
"""
from collections import Counter


def can_be_made_palindromic(word):
    odd_freq = 0
    for freq in Counter(word).values():
        if freq % 2 != 0:
            odd_freq += 1
            if odd_freq > 1:
                return False
    return True


if __name__ == "__main__":
    word = "aabbcd"
    print(int(can_be_made_palindromic(word)))
