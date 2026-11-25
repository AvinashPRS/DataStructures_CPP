"""
Problem:
    Rabin Karp Algo

Input:
    patt: string pattern
    text: string text

Output:
    matched indices: list of indices

TC: Avg case: O(m + n)
    Worst case: O(mn)
    m: length of pattern
    n: length of text
"""


def rabin_karp(text, patt):
    """
    The idea behind Rabin Karp is we use a hash function to compute the
    hash value of the pattern and text window. When the hash value of the
    window matches that of the pattern, then we check if the pattern is actually
    present or not.

    For hash function we use the number formed by the chars in the given base.
    (Python ints are arbitrary precision so no modulus is needed for overflow.)
    """
    if len(patt) > len(text) or not patt:
        return []

    base = 26
    M = len(patt)
    N = len(text)

    # base ^ (length of pattern - 1)
    power_patt = 1
    hash_patt = 0
    hash_text = 0
    indices = []

    # find the hash value of the pattern and the first window of text
    for i in range(M):
        power_patt = base * power_patt if i else 1
        hash_patt = hash_patt * base + ord(patt[i])
        hash_text = hash_text * base + ord(text[i])

    # traverse through the text using the window
    for i in range(N - M + 1):
        # check if the hash values match, then check if it actually matches text
        if hash_patt == hash_text and text[i:i + M] == patt:
            indices.append(i)

        # adjust the hash value for the new window
        if i + M < N:
            hash_text = (hash_text - power_patt * ord(text[i])) * base + ord(text[i + M])

    return indices


if __name__ == "__main__":
    text = "abaacab"
    patt = "a"
    print(" ".join(str(i) for i in rabin_karp(text, patt)))
