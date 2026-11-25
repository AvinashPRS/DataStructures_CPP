"""
Given an array of strings, find the length of the longest subarray which has distinct elements.
Input: array of strings
Output: int

Solution:
    Keep track of the starting index of the current duplicate-free subarray and the longest length.

    For each index 'i':
    1. If arr[i] is a duplicate whose last occurrence is inside the current subarray:
            the subarray can't continue, so update the longest length and move the start
            to one past the last occurrence of the duplicate.
    2. Otherwise it is distinct, continue.

    Update the most recent index of the current word in the hash table.

    TC: O(n)
    SC: O(m), m: no. of distinct words
"""


def longest_distinct_value_subarray(arr):
    recent_idx = {}       # most recent index of each word
    start_dup_free = 0    # start of the duplicate-free subarray
    longest_len = 0

    for i, word in enumerate(arr):
        if word in recent_idx and recent_idx[word] >= start_dup_free:
            longest_len = max(longest_len, i - start_dup_free)
            start_dup_free = recent_idx[word] + 1
        recent_idx[word] = i

    # length only gets updated on a duplicate, so account for the final subarray
    return max(longest_len, len(arr) - start_dup_free)


if __name__ == "__main__":
    arr = ["I", "apple", "kiwi", "banana", "was", "apple", "orange", "apple", "banana", "new",
           "new", "new"]
    print(f"Length: {longest_distinct_value_subarray(arr)}")
