"""
Calculate the length of the longest increasing subsequence in a list.

The longest increasing subsequence problem is to find a subsequence of a given
sequence in which the elements are in sorted order, lowest to highest, and which
is as long as possible. It is not necessarily contiguous, or unique.
This implementation is O(n^2); the problem is solvable in O(n log n).
"""


def lis(a):
    """Return the length of the longest increasing subsequence in a"""
    n = len(a)
    lis_len = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and lis_len[i] < lis_len[j] + 1:
                lis_len[i] = lis_len[j] + 1
    return max(lis_len, default=0)


def test():
    a = [15, 21, 2, 3, 4, 5, 8, 4, 1, 1]
    assert lis(a) == 5  # The longest increasing subsequence is {2,3,4,5,8}
    print("Self-test implementations passed!")


if __name__ == "__main__":
    n = int(input("Enter size of array: "))
    a = list(map(int, input("Enter array elements: ").split()))[:n]
    print(f"\nThe result is: {lis(a)}")
    test()  # run self-test implementations
