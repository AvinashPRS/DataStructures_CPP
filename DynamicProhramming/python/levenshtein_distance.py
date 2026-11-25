"""
Levenshtein distance is the no. of edits to make a string 'a' convert to string 'b'.
The edits can be: insert, delete and substitute chars.
Find the min. levenshtein distance for converting string 'a' to 'b'.

Solution:
    Start with the last character of both strings.
    If the chars are same, go for the next char in both the strings.
    If they are different, try all three operations and take the min:
        F(n, m) = 1 + min {
            insertion: F(n, m-1)
            deletion: F(n-1, m)
            substitution: F(n-1, m-1)
        }

    TC: O(nm), n: string a length, m: string b length
    SC: O(nm)
"""


def min_levenshtein_distance_helper(a, a_idx, b, b_idx, cache):
    """helper for finding the levenshtein distance using memoization"""
    # if string 'a' has finished, remaining chars of 'b' need to be inserted
    if a_idx < 0 and b_idx >= 0:
        return b_idx + 1
    # if string 'b' has finished, then remaining 'a' chars need to be deleted
    if b_idx < 0 and a_idx >= 0:
        return a_idx + 1
    # if both are finished, then no edits are required
    if a_idx < 0 and b_idx < 0:
        return 0

    # if current chars of both the strings are same, then check the next chars
    if a[a_idx] == b[b_idx]:
        cache[a_idx][b_idx] = min_levenshtein_distance_helper(a, a_idx - 1, b, b_idx - 1, cache)
        return cache[a_idx][b_idx]

    if cache[a_idx][b_idx] == 0:
        substitute_op = min_levenshtein_distance_helper(a, a_idx - 1, b, b_idx - 1, cache)
        delete_op = min_levenshtein_distance_helper(a, a_idx - 1, b, b_idx, cache)
        insert_op = min_levenshtein_distance_helper(a, a_idx, b, b_idx - 1, cache)

        cache[a_idx][b_idx] = 1 + min(substitute_op, delete_op, insert_op)

    return cache[a_idx][b_idx]


def min_levenshtein_distance(a, b):
    """finds the min levenshtein distance to convert first string to second"""
    # each entry (i, j) stores min levenshtein distance till that index
    cache = [[0] * len(b) for _ in range(len(a))]
    return min_levenshtein_distance_helper(a, len(a) - 1, b, len(b) - 1, cache)


if __name__ == "__main__":
    print(min_levenshtein_distance("aab", "a"))
