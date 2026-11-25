"""
    Given K, find the smallest k numbers of the form a + b*Root(2),
    where a, b: non-neg int.
    General form : a + b*Root(q), q: irrational number and a,b : non-neg int
    Solution:
        Since 'a' and 'b' can have only int values, the first min values are:
        0 + 0*Root(2), then 1 + 0*Root(2), 0 + 1*Root(2).
        Every time we extract the min candidate and push two new candidates
        (a + 1, b) and (a, b + 1).
        The C++ version uses std::set (a BST, which also removes duplicates by
        value); here a min-heap plus a "seen" set gives the same result.
        TC: O(klogk)
        SC: O(k)
"""
import heapq
import math


class NumberForm:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.value = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.value < other.value


def find_k_smallest_numbers(k):
    """Finds the K smallest numbers of form a + b * Root(2)."""
    candidates = [NumberForm(0, 0)]
    seen = {(0, 0)}
    result = []
    while k > 0 and candidates:
        k -= 1
        smallest = heapq.heappop(candidates)
        result.append(smallest)
        for a, b in ((smallest.a + 1, smallest.b), (smallest.a, smallest.b + 1)):
            if (a, b) not in seen:
                seen.add((a, b))
                heapq.heappush(candidates, NumberForm(a, b))
    return result


def main():
    for n in find_k_smallest_numbers(5):
        print("%d + %d * Root(2) : %g" % (n.a, n.b, n.value))


if __name__ == "__main__":
    main()
