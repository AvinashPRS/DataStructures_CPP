"""
There is a stream of string words coming, find the 'k' largest strings.

Input: streaming strings
Output: k largest strings

Solution:
    Use a min-heap of size 'k' keyed on string length. It always has the shortest
    string at the top. Push the current string and if heap size > k, pop the smallest.

    TC: O(nlogk + nL), L = longest string
    SC: O(kL)
"""
import heapq


def find_k_largest_strings(stream, k):
    if k <= 0:
        return []

    min_heap = []   # entries: (len, arrival order, string)
    for order, s in enumerate(stream):
        heapq.heappush(min_heap, (len(s), order, s))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    k_largest = []
    while min_heap:
        k_largest.append(heapq.heappop(min_heap)[2])
    return k_largest


if __name__ == "__main__":
    txt = "apple banana cake lemon apple toffee"
    k = 3
    # iter(txt.split()) plays the role of the istringstream
    print(" ".join(find_k_largest_strings(iter(txt.split()), k)))
