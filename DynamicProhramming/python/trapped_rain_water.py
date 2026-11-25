"""Trapped Rainwater Problem using the two-pointer technique."""


def trapped_rainwater(heights):
    """
    heights: list representing the heights of walls
    Return value: the amount of trapped rainwater
    """
    n = len(heights)
    if n <= 2:
        return 0

    left, right = 0, n - 1
    left_max = right_max = trapped_water = 0

    # two pointer method to calculate trapped rainwater
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                trapped_water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                trapped_water += right_max - heights[right]
            right -= 1
    return trapped_water


def test():
    assert trapped_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trapped_rainwater([3, 0, 2, 0, 4]) == 7
    assert trapped_rainwater([5, 1, 5]) == 4
    print("All trapping rainwater tests successfully passed!")


if __name__ == "__main__":
    test()
