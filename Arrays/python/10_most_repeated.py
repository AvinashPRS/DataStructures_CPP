"""
Find the most repeated number in an array where every value is in [0, k-1] and k <= n,
using O(1) extra space.

Solution:
    For each element, add k to a[a[i] % k]. The index holding the largest value is
    the most repeated number. Finally restore the array with a[i] % k.

    TC: O(n)
    SC: O(1)
"""


def find_most_repeated(a, k):
    n = len(a)
    for i in range(n):
        # a[i] may already have k added to it, so take % k for the original value
        index = a[i] % k
        a[index] += k

    most_repeated = -1
    max_value = float("-inf")
    for i in range(n):
        if a[i] > max_value:
            most_repeated = i
            max_value = a[i]
        # Restore the original value
        a[i] %= k

    return most_repeated


if __name__ == "__main__":
    a = [2, 4, 0, 5, 2, 1, 9, 6, 8, 9, 2, 7]
    k = 10  # all values are < k and k <= n

    result = find_most_repeated(a, k)
    print("Input :", *a)
    print("Most repeated element =", result)

    assert result == 2, "Test failed"
    print("Test passed")
