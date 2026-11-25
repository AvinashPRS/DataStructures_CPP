"""Encode a list of strings into one string and decode it back. O(n).
'$' is escaped as '$$' and each string is terminated by '$x'."""


class Solution:
    def encode(self, strs):
        ans = []
        for s in strs:
            for c in s:
                if c == "$":
                    ans.append(c)
                ans.append(c)
            ans.append("$x")
        return "".join(ans)

    def decode(self, s):
        ans = []
        i, n = 0, len(s)
        while i < n:
            cur = []
            while i < n:
                if s[i] != "$":
                    cur.append(s[i])
                elif i + 1 < n and s[i + 1] == "$":
                    cur.append(s[i])
                    i += 1
                else:
                    i += 2
                    break
                i += 1
            ans.append("".join(cur))
        return ans


def show(label, strs):
    out = label + "["
    for idx, s in enumerate(strs):
        out += s + " "
        if s != strs[-1]:
            out += ", "
    print(out + "]")


def main():
    strs = ["we", "say", ":", "yes"]
    show("Input: ", strs)
    sol = Solution()
    encoded_string = sol.encode(strs)
    decoded_strings = sol.decode(encoded_string)
    show("Ouput: ", decoded_strings)


if __name__ == "__main__":
    main()
