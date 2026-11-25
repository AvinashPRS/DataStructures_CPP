"""
Given a set of words, group the words which are anagrams of each other.

Input: array of string
Output: 2d array of strings

Solution:
    Anagrams have the same characters with the same frequencies. So we can sort each word and
    use it as a key in a hash table. Words with the same sorted key go in the same group.
    Finally drop groups that contain only one word.

    TC: O(n * mlogm), n: no. of words, m: max length of a word
    SC: O(n), n: no. of words
"""
from collections import defaultdict


def group_anagrams(arr):
    """Groups words that have at least one anagram."""
    anagrams = defaultdict(list)

    # build groups
    for word in arr:
        anagrams["".join(sorted(word))].append(word)

    # remove groups containing only one word
    return {k: v for k, v in anagrams.items() if len(v) >= 2}


def print_anagram_groups(groups):
    for words in groups.values():
        print(" ".join(words))


if __name__ == "__main__":
    arr = ["dog", "god", "kite", "debitcard", "badcredit"]
    print_anagram_groups(group_anagrams(arr))
