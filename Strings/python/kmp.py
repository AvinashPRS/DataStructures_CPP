"""
KMP:
    Using brute force approach for string matching involves using every index for starting the search in case of
    failure. To avoid doing that each time we need to decide which index to start with we just check
    till which last character do we have matching results in pattern, then the next character is matched
    with current char of text.

TC: O(n + m)
SC: O(n), n: pattern length, m: string length
"""


def compute_longest_proper_suffix(patt):
    """Computes LPS (longest proper prefix which is also a suffix) array"""
    i, j = 1, 0
    lps = [0] * len(patt)

    while i < len(patt):
        # if the chars match
        if patt[i] == patt[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

    return lps


def kmp(text, pattern):
    """KMP algorithm: finds all the matching indices"""
    if len(text) < len(pattern) or len(pattern) <= 0 or len(text) <= 0:
        return []

    # compute the lps array
    lps = compute_longest_proper_suffix(pattern)

    i = j = 0
    matches = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            # string match found
            if j == len(pattern):
                matches.append(i - j)
                # decide the position of j to start matching
                j = lps[j - 1]
        elif j != 0:  # they don't match
            j = lps[j - 1]
        else:
            i += 1

    return matches


if __name__ == "__main__":
    pattern = "abac"
    text = "aabcabachabacsb"

    print(" ".join(str(a) for a in kmp(text, pattern)))
