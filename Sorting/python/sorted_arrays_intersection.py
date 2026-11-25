"""
Given two sorted arrays, return their intersection.

Solution:
    Use two indices and walk both arrays until one is finished:
      - advance the index of the smaller value
      - if values are equal, add to the result and advance both
    TC: O(n)

Note: like the C++ original, duplicates present in BOTH arrays are kept
(e.g. [6, 6] and [6] -> [6]; [23, 23] and [23] -> [23]).
"""


def find_intersection(a, b):
    intersection = []
    i = j = 0  # i is for a, j is for b

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            intersection.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return intersection


if __name__ == "__main__":
    a = [2, 3, 6, 8, 22, 23, 23, 78, 99]
    b = [6, 6, 23, 99]
    print(*find_intersection(a, b))
