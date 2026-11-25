"""
[Variant] Given an input stream of strings and a set of string keywords.
Find the smallest subarray which contains the keywords.

Input: stream of strings
Output: range indices of subarray

Solution:
    Since the input is streaming we use a doubly linked list for storing the index of keywords.
    Every time a keyword is seen we add its index to the back of the list; in case it was already
    seen once we remove that node and add the new recent index as the last node.
    The first node of the list is the oldest seen keyword. For each new streamed word, we compute the
    diff between the first node index and the current index; if the subarray length is smaller than the
    current best and all the keywords have been covered, update the subarray index.

    In Python, an OrderedDict (keyword -> last seen index) plays the role of
    list + hash-table-of-iterators: deleting and re-inserting a key moves it to the end in O(1).

    TC: O(n)
    SC: O(m), m: no. of keywords
"""
import io
from collections import OrderedDict


def smallest_streamed_subarray_with_keywords(stream_in, keywords):
    """Finds the (start, end) of the smallest subarray containing all keywords."""
    keywords_subarray = (-1, -1)

    # keyword -> latest index, ordered from oldest seen to most recently seen
    idx = OrderedDict()

    curr = 0
    for line in stream_in:
        for s in line.split():
            if s in keywords:
                # remove old position (if any) and append the latest index at the back
                idx.pop(s, None)
                idx[s] = curr

            # if all the keywords have been covered, check if current subarray is smallest
            if len(idx) == len(keywords):
                front = next(iter(idx.values()))
                if keywords_subarray == (-1, -1) or \
                        (curr - front) < (keywords_subarray[1] - keywords_subarray[0]):
                    keywords_subarray = (front, curr)

            curr += 1
    return keywords_subarray


if __name__ == "__main__":
    text = "apple banana orange apple dog banana apple cat orange banana"
    stream = io.StringIO(text)
    keywords = {"apple", "banana", "orange"}

    result = smallest_streamed_subarray_with_keywords(stream, keywords)
    print(f"Smallest Subarray Range: [{result[0]}, {result[1]}]")
    # Expected: [0, 2] -> "apple banana orange"
