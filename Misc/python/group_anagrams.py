"""Group Anagrams using a hash map. O(N K log K)."""


class Solution:
    def groupAnagrams(self, strs):
        m = {}
        ans = []
        for s in strs:
            key = "".join(sorted(s))
            if key not in m:
                m[key] = len(ans)
                ans.append([])
            ans[m[key]].append(s)
        ans.reverse()
        return ans


def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: [{', '.join(words)}]")
    result = Solution().groupAnagrams(words)
    print("Output: [" + ", ".join("[" + ", ".join(g) + "]" for g in result) + "]")


if __name__ == "__main__":
    main()
