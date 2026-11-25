"""Check whether a list contains a duplicate using a hash map."""


class Solution:
    def containsDuplicate(self, nums):
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                return True
        return False


def main():
    nums = [1, 2, 3, 4, 5, 6, 2]
    if Solution().containsDuplicate(nums):
        print("Contains Duplicate")
    else:
        print("No Duplicate")


if __name__ == "__main__":
    main()
