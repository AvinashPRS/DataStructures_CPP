"""
Given an array of strings and a set of keywords, find the smallest subarray which contains
all the keywords.

Input: array of strings
Output: range indices of subarray

Solution:
    Sliding window with two indices. A hash table holds keyword -> count still required.
    Move the right index until all keywords are covered. Then move the left index to shrink
    the window while the keywords are still covered. Whenever coverage breaks, resume moving
    the right index. Track the window with min |end - start|.

    TC: O(n)
    SC: O(m), m: no. of keywords
"""
from collections import Counter


def smallest_subarray_with_keywords(arr, keywords):
    keywords_subarray = (-1, -1)

    keyword_freq = Counter(keywords)   # counts still required (can go negative for extras)
    num_keywords_cover = len(keywords)

    left = 0
    for right, word in enumerate(arr):
        # a needed (not excess) keyword reduces what's left to cover
        if word in keywords:
            keyword_freq[word] -= 1
            if keyword_freq[word] >= 0:
                num_keywords_cover -= 1

        # all keywords covered: shrink from the left
        while num_keywords_cover == 0:
            if keywords_subarray == (-1, -1) or \
                    right - left < keywords_subarray[1] - keywords_subarray[0]:
                keywords_subarray = (left, right)

            if arr[left] in keywords:
                keyword_freq[arr[left]] += 1
                if keyword_freq[arr[left]] > 0:
                    num_keywords_cover += 1
            left += 1

    return keywords_subarray


if __name__ == "__main__":
    arr = ["I", "apple", "kiwi", "banana", "was", "apple", "orange", "apple", "banana", "new",
           "new", "new"]
    keywords = {"banana", "apple"}

    start, end = smallest_subarray_with_keywords(arr, keywords)
    print(f"Start: {start}, Second: {end}")
