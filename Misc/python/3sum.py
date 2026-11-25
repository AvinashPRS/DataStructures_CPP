"""3Sum: find all unique triplets that sum to zero."""


class Solution:
    def threeSum(self, nums):
        result = []
        n = len(nums)
        if n < 3:
            return result

        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    k -= 1
        return result


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = [{', '.join(map(str, nums))}]")
    result = Solution().threeSum(nums)
    print("Output: [" + ", ".join("[" + ", ".join(map(str, v)) + "]" for v in result) + "]")


if __name__ == "__main__":
    main()
