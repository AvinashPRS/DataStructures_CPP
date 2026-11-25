"""
Given an array of strings, find the closest distance between two equal words in the array.

Input: array of string
Output: int

Solution:
    Use a hash table: key: string, value: last index seen
    min_dist = INF
    For each entry in the array:
        if present in hash table:
            dist = current index - stored index
            min_dist = min(min_dist, dist)
        update the index in the hash table

    TC: O(n)
    SC: O(m), m: no. of distinct words
"""
import math


def find_closest_words_distance(arr):
    closest_dist = math.inf
    last_word_idx = {}

    for i, word in enumerate(arr):
        if word in last_word_idx:
            closest_dist = min(closest_dist, i - last_word_idx[word])
        last_word_idx[word] = i
    return closest_dist


if __name__ == "__main__":
    arr = ["I", "apple", "banana", "was", "apple", "orange", "apple", "banana"]
    print(find_closest_words_distance(arr))
