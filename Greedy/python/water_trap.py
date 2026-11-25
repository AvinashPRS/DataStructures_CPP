"""
Given a list of heights with their index positions as x-coordinates, find the pair of heights
which makes the largest volume for trapping water between them. Assume the width to be 1 unit.

Input: list of numbers
Output: max volume

Solution:
    Start with the two end points for max width, then move inward from the shorter side
    while tracking the maximum volume. If the heights are the same, move both ends.
TC: O(n)
"""


def max_water_volume(heights):
    """Finds the maximum volume of water that can be stored."""
    max_vol = 0

    # we traverse from both ends
    i, j = 0, len(heights) - 1

    while i < j:
        max_vol = max(max_vol, (j - i) * min(heights[i], heights[j]))

        # check in which direction to move
        if heights[i] < heights[j]:
            i += 1
        elif heights[i] > heights[j]:
            j -= 1
        else:
            i += 1
            j -= 1

    return max_vol


if __name__ == "__main__":
    heights = [1, 2, 1, 3, 34, 4, 5, 6, 2, 51, 3, 1, 13, 2, 1, 24, 4, 1]
    print(f"Max water volume that would be trapped: {max_water_volume(heights)}")
