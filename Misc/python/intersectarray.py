"""Intersection of two sorted arrays (distinct values only)."""


class Solution:
    def IntersectTwoSortedArrays(self, arr1, arr2):
        result = []
        l1 = l2 = 0
        while l1 < len(arr1) and l2 < len(arr2):
            if arr1[l1] == arr2[l2] and (l1 == 0 or arr1[l1] != arr1[l1 - 1]):
                result.append(arr1[l1])
                l1 += 1
                l2 += 1
            elif arr1[l1] < arr2[l2]:
                l1 += 1
            else:
                l2 += 1
        return result


def main():
    arr1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    arr2 = [5, 5, 6, 8, 8, 9, 10, 10]
    ans = Solution().IntersectTwoSortedArrays(arr1, arr2)
    print("Intersection:")
    print("".join(f"{x} " for x in ans))


if __name__ == "__main__":
    main()
