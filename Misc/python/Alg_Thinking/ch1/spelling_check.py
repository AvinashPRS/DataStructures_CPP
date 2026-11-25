"""Spelling Check: which single character deletion turns s1 into s2."""
import sys


def prefix_length(s1, s2):
    # s1, s2 are 1-indexed with a sentinel at the end
    i = 1
    while s1[i] == s2[i]:
        i += 1
    return i - 1


def suffix_length(s1, s2, length):
    i = length
    while i >= 2 and s1[i] == s2[i - 1]:
        i -= 1
    return length - i


def main():
    s1 = sys.stdin.readline().rstrip("\n")
    s2 = sys.stdin.readline().rstrip("\n")
    length = len(s1)
    # 1-indexed with '\0' sentinels (like the C version)
    a = "\0" + s1 + "\0"
    b = "\0" + s2 + "\0\0"
    prefix = prefix_length(a, b)
    suffix = suffix_length(a, b, length)
    total = (prefix + 1) - (length - suffix) + 1
    if total < 0:
        total = 0
    print(total)
    if total > 0:
        print(" ".join(str(i + length - suffix) for i in range(total)))


if __name__ == "__main__":
    main()
