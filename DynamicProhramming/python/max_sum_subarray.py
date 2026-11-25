"""
Given a list of integers, find the maximum sum subarray.

Solution:
    For any index 'i', the max sum till there is the total sum till there minus the
    min sum prefix. We keep track of the total sum and min prefix sum, and at every
    index check if total sum - min prefix sum gives us the max value.
    TC: O(n)
"""


def find_max_array_sum(arr):
    """finds the max subarray sum value"""
    max_sum = 0  # tracks max sum
    total = 0    # tracks total sum
    min_sum = 0  # tracks sum of min value prefix

    for el in arr:
        # compute the total sum till current index
        total += el

        # track the min sum value prefix till current index
        if total < min_sum:
            min_sum = total
        # check if removing some min value earlier prefix gives a max value subarray
        if total - min_sum > max_sum:
            max_sum = total - min_sum
    return max_sum


if __name__ == "__main__":
    arr = [-7, 2, 3, -6, 5, 6]
    print(find_max_array_sum(arr))
