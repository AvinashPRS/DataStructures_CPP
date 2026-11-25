"""Check whether two strings are anagrams by sorting."""


class Solution:
    def isAnagram(self, s, t):
        # Different lengths can never be anagrams
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


def main():
    sol = Solution()
    print("Anagram" if sol.isAnagram("anagram", "nagaram") else "Not Anagram")
    print("Anagram" if sol.isAnagram("rat", "car") else "Not Anagram")


if __name__ == "__main__":
    main()
