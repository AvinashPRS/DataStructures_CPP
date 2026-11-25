"""Find the minimum in a rotated sorted array - binary search, O(log n)."""


class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            m = (left + right) // 2  # middle index
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m
        return nums[left]


def main():
    nums = [3, 4, 5, 1, 2]
    print(f"Input: nums = [{', '.join(map(str, nums))}]")
    print(f"Output: {Solution().findMin(nums)}")


if __name__ == "__main__":
    main()
