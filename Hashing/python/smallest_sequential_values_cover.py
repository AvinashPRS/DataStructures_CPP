"""
Given an array of strings and a list of keywords, find the smallest subarray which contains
the keywords in the given order (sequentially).

Input: array of strings
Output: range indices of subarray

Solution:
    Index the keywords from 0. Keep:
      - keyword_idx: keyword -> its 0-based position in the keyword list
      - latest_occurrence[j]: latest index where keyword j was seen
      - smallest_subarray_length[j]: length of the shortest subarray ending at the latest
        occurrence of keyword j that covers keywords 0..j in order

    Initially all lengths are INF. When keyword j (> 0) is seen, it can only extend a cover
    if keyword j-1 has already been covered; then
        length[j] = length[j-1] + (i - latest_occurrence[j-1]).
    When the last keyword is seen, check against the global minimum.

    TC: O(n)
    SC: O(m), m: no. of keywords
"""
import math


def smallest_sequential_subarray_with_keywords(arr, keywords):
    keyword_idx = {kw: i for i, kw in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    smallest_subarray_length = [math.inf] * len(keywords)

    global_smallest = math.inf
    keywords_subarray = (-1, -1)

    for i, word in enumerate(arr):
        if word not in keyword_idx:
            continue
        idx = keyword_idx[word]

        if idx == 0:
            # the starting keyword, length is 1
            smallest_subarray_length[idx] = 1
        elif smallest_subarray_length[idx - 1] != math.inf:
            # keywords before this one have been covered
            smallest_subarray_length[idx] = (smallest_subarray_length[idx - 1]
                                             + i - latest_occurrence[idx - 1])
        latest_occurrence[idx] = i

        # last keyword: check if this subarray is the global minimum
        if idx == len(keywords) - 1 and smallest_subarray_length[idx] < global_smallest:
            global_smallest = smallest_subarray_length[idx]
            keywords_subarray = (i - global_smallest + 1, i)

    return keywords_subarray


if __name__ == "__main__":
    arr = ["I", "apple", "kiwi", "banana", "was", "banana", "apple", "kiwi", "kiwi", "was",
           "apple", "orange", "apple", "banana", "apple", "new", "new", "new"]
    keywords = ["banana", "was", "apple"]

    start, end = smallest_sequential_subarray_with_keywords(arr, keywords)
    print(f"Start: {start}, Second: {end}")
