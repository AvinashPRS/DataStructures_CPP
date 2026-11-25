"""
Given a list of ints, find the longest increasing (non-decreasing) subsequence.

Solution:
    We store the longest length ending at each index. For each index, the longest
    increasing subsequence at that index is at least 1 (the element itself). We look
    at the previous indices for the longest length whose element is not greater than
    the current element:
        length[i] = max(length[j] + 1, length[i]) for j < i

    TC: O(n^2)
    SC: O(n)
"""


def longest_increasing_subsequence(arr):
    longest_length = 0

    # for storing longest length ending at each index
    longest_increasing_length = [1] * len(arr)
    # optional for storing the actual subsequence
    subarray = [-1] * len(arr)
    longest_length_ending_idx = 0

    for i in range(1, len(arr)):
        # check for the longest length in previous elements
        for j in range(i):
            # update the longest length if necessary
            if arr[j] <= arr[i]:
                if longest_increasing_length[j] + 1 > longest_increasing_length[i]:
                    longest_increasing_length[i] = longest_increasing_length[j] + 1
                    subarray[i] = j

        if longest_increasing_length[i] > longest_length:
            longest_length_ending_idx = i
        longest_length = max(longest_length, longest_increasing_length[i])

    # it will print in reverse form
    while longest_length_ending_idx != -1:
        print(arr[longest_length_ending_idx], end=" ")
        longest_length_ending_idx = subarray[longest_length_ending_idx]
    print()
    return longest_length


if __name__ == "__main__":
    arr = [1, 8, 3, 11, 2, 10, 6, 14, 2, 9]
    print(longest_increasing_subsequence(arr))
