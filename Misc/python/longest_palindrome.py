"""Length of the longest palindromic substring (expand around centre)."""
import sys


def handle_error():
    print("Test failed")
    sys.exit(1)


def find_longest_palindrome(str1):
    n = len(str1)
    max_pal_len = 0
    for pos in range(n):
        # Odd length palindromes centred at pos
        left, right = pos - 1, pos + 1
        cur_pal_len = 1
        while left >= 0 and right <= n - 1 and str1[left] == str1[right]:
            cur_pal_len += 2
            left -= 1
            right += 1
        max_pal_len = max(max_pal_len, cur_pal_len)

        # Even length palindromes centred between pos and pos + 1
        if pos + 1 < n and str1[pos] == str1[pos + 1]:
            left, right = pos - 1, pos + 2
            cur_pal_len = 2
            while left >= 0 and right <= n - 1 and str1[left] == str1[right]:
                cur_pal_len += 2
                left -= 1
                right += 1
            max_pal_len = max(max_pal_len, cur_pal_len)
    return max_pal_len


def test_01(str1, expected_result):
    result = find_longest_palindrome(str1)
    print(f"Length of longest palindrome in {str1} = {result}")
    if result != expected_result:
        handle_error()


def main():
    test_01("RACECAR", 7)
    test_01("AABB", 2)
    test_01("ABBA", 4)
    test_01("ACBBDA", 2)
    test_01("ABCDE", 1)  # a single character is a palindrome
    print("Test passed")


if __name__ == "__main__":
    main()
