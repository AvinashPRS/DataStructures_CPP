"""Merge Sorted Array (LeetCode 88): merge nums2 into nums1 in place,
writing from the back."""


class Solution:
    def merge(self, nums1, m, nums2, n):
        index_to_write = m + n - 1
        i = m - 1  # last element in the first list
        j = n - 1  # last element in the second list
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index_to_write] = nums1[i]
                i -= 1
            else:
                nums1[index_to_write] = nums2[j]
                j -= 1
            index_to_write -= 1
        while i >= 0:
            nums1[index_to_write] = nums1[i]
            i -= 1
            index_to_write -= 1
        while j >= 0:
            nums1[index_to_write] = nums2[j]
            j -= 1
            index_to_write -= 1


def main():
    pass  # the C++ main does nothing


if __name__ == "__main__":
    main()
