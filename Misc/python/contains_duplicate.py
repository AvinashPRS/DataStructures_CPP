"""Contains Duplicate - using a hash set, O(n)."""


class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


def main():
    nums = [1, 2, 3, 1]
    print(f"Input: nums = [{', '.join(map(str, nums))}]")
    print(f"Output: {str(Solution().containsDuplicate(nums)).lower()}")


if __name__ == "__main__":
    main()
