"""
Given two sources of chars, s1 and s2. Check if s1 can be formed from s2.
Input: string, string
Output: bool

Solution:
    Create a hash table with chars of s1 and for values have the frequency of each char.
    Then do a traversal of s2 and for each char decrement count in hash table for that char;
    if the freq becomes zero, remove that char. If the hash table becomes empty then return true,
    else if after traversal the hash table is not empty return false.

    TC: O(n + m), n: chars in s1, m: chars in s2
    SC: O(m), m: unique chars in s1
"""
from collections import Counter


def can_s2_create_s1(s1, s2):
    """Checks if s1 can be made using the chars of s2."""
    char_freq = Counter(s1)

    if not char_freq:
        return True

    for c in s2:
        if c in char_freq:
            char_freq[c] -= 1
            if char_freq[c] == 0:
                del char_freq[c]
            if not char_freq:
                return True

    return not char_freq


if __name__ == "__main__":
    s1 = "aadd"
    s2 = "afad"
    print(int(can_s2_create_s1(s1, s2)))
