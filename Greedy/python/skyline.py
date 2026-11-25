"""
Given a list of numbers representing the heights of buildings. Find the
area of the largest rectangle that can be made out of these buildings.

Input: list of numbers
Output: Area of largest rectangle

Solution:
    For building 'i' the largest rectangle is the one created by buildings of at least the same height
    on either side. So for each building we need to find the blocking building on either side.
    Use a stack: if the stack is empty or the current building is taller than the top, push it.
    Otherwise pop until the stack top is shorter than the current building, computing the
    area supported by each popped building.
TC: O(n)
"""


def find_largest_rectangle(heights):
    max_area = 0
    buildings = []  # stack of indices

    for i, h in enumerate(heights):
        # pop the buildings at least as tall as the current one and compute their area
        while buildings and heights[buildings[-1]] >= h:
            idx = buildings.pop()
            left = buildings[-1] + 1 if buildings else 0
            max_area = max(max_area, heights[idx] * (i - left))

        # push the current building
        buildings.append(i)

    # area for the remaining buildings
    n = len(heights)
    while buildings:
        idx = buildings.pop()
        left = buildings[-1] + 1 if buildings else 0
        max_area = max(max_area, heights[idx] * (n - left))

    return max_area


if __name__ == "__main__":
    heights = [1, 14, 32, 54, 6, 3, 42, 6, 9, 2, 1, 3]
    print(find_largest_rectangle(heights))
