"""
Given an array of strings, find the K most frequent strings.

Input: array of strings
Output: array of strings

Solution:
    Sol1: Use a hash table for counts, then sort in non-increasing order and return the first K terms.
          TC: O(n + mlogm), n: no. of words, m: distinct words
          SC: O(m)

    Sol2: Use a min-heap of k elements to reduce TC to O(n + mlogk), SC: O(m + k).
          Take the frequency count, then traverse the word frequencies; if the frequency is larger
          than the heap root, remove root and insert the word. In the end the heap holds the k most
          frequent words.

    Sol3: Quickselect on the frequency table for the kth most frequent word, then prune after 'k'.
          TC: avg O(n + m), worst O(n + m^2), SC: O(m)
"""
import heapq
from collections import Counter


def k_frequent_words(arr, k):
    """Solution 1: sort by frequency. TC: O(n + mlogm)"""
    freq = list(Counter(arr).items())
    # sort the words by frequency (the count is used as the sort key)
    freq.sort(key=lambda p: p[1], reverse=True)
    return freq[:k]


def k_frequent_words_pqueue(arr, k):
    """Solution 2: min-heap of size k. TC: O(n + mlogk)"""
    pq = []  # min-heap of (count, word)
    for word, count in Counter(arr).items():
        if len(pq) >= k:
            if pq[0][0] < count:
                heapq.heapreplace(pq, (count, word))
        else:
            heapq.heappush(pq, (count, word))

    k_freq = []
    while pq:
        count, word = heapq.heappop(pq)
        k_freq.append((word, count))
    return k_freq


if __name__ == "__main__":
    arr = ["I", "apple", "banana", "was", "apple", "orange", "apple", "banana", "new",
           "new", "new"]

    for w, _ in k_frequent_words(arr, 2):
        print(w)
    print()
    for w, _ in k_frequent_words_pqueue(arr, 2):
        print(w)
