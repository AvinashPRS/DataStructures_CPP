"""
Computes the length of the longest common string which can be created from two
input strings by removing characters from them (i.e. longest common subsequence).

O(len(a) * len(b)) time and memory (full 2D table).
"""
from collections import namedtuple


def longest_common_string_length(string_a, string_b):
    size_a = len(string_a)
    size_b = len(string_b)
    sub_sols = [[0] * (size_b + 1) for _ in range(size_a + 1)]

    for pos_a in range(size_a - 1, -1, -1):
        for pos_b in range(size_b - 1, -1, -1):
            if string_a[pos_a] == string_b[pos_b]:
                sub_sols[pos_a][pos_b] = 1 + sub_sols[pos_a + 1][pos_b + 1]
            else:
                sub_sols[pos_a][pos_b] = max(sub_sols[pos_a + 1][pos_b],
                                             sub_sols[pos_a][pos_b + 1])

    return sub_sols[0][0]


TestCase = namedtuple("TestCase", ["string_a", "string_b", "common_string_len"])


def get_test_cases():
    return [TestCase("", "", 0),
            TestCase("ab", "ab", 2),
            TestCase("ab", "ba", 1),
            TestCase("", "xyz", 0),
            TestCase("abcde", "ace", 3),
            TestCase("BADANA", "ANADA", 3),
            TestCase("BADANA", "CANADAS", 3),
            TestCase("a1a234a5aaaa6", "A1AAAA234AAA56AAAAA", 6),
            TestCase("123x", "123", 3),
            TestCase("12x3x", "123", 3),
            TestCase("1x2x3x", "123", 3),
            TestCase("x1x2x3x", "123", 3),
            TestCase("x12x3x", "123", 3)]


def tests():
    test_cases = get_test_cases()
    assert len(test_cases) > 0
    for tc in test_cases:
        assert longest_common_string_length(tc.string_a, tc.string_b) == tc.common_string_len
        # result must be the same when the arguments are flipped
        assert longest_common_string_length(tc.string_b, tc.string_a) == tc.common_string_len
        # result must be the same when the inputs are reversed
        assert longest_common_string_length(tc.string_a[::-1], tc.string_b[::-1]) == tc.common_string_len

    print("All tests have successfully passed!")


if __name__ == "__main__":
    tests()
