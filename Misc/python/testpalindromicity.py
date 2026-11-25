"""Valid Palindrome: ignore non-alphanumeric characters and case."""


class Solution:
    @staticmethod
    def is_alphanumeric(ch):
        return ch.isascii() and ch.isalnum()

    def isPalindrome(self, s):
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not self.is_alphanumeric(s[left]):
                left += 1
                continue
            if not self.is_alphanumeric(s[right]):
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


def main():
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    print("\n=======SUCCESS======Palindrome\n ")


if __name__ == "__main__":
    main()
