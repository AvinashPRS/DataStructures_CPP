"""Container With Most Water - two pointers, O(n)."""


class Solution:
    def maxArea(self, height):
        ans, left, right = 0, 0, len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1   # move the smaller edge
            else:
                right -= 1  # move the larger edge
        return ans


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: height = [{', '.join(map(str, height))}]")
    print(f"Output: {Solution().maxArea(height)}")


if __name__ == "__main__":
    main()
