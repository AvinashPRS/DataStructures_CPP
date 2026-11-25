"""Word segmentation using a dp[] of segmentable prefixes, returning words in order."""


def longest_dict_word_length(dictionary):
    return max((len(word) for word in dictionary), default=0)


def can_string_be_decomposed(s, dictionary):
    n = len(s)
    if n == 0:
        return []

    # dp[i] is True if s[0...i-1] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string is valid

    # parent_length[i] stores the length of the word that ends at index i-1
    parent_length = [-1] * (n + 1)

    longest_word_len = longest_dict_word_length(dictionary)

    # Outer loop moves across the length of the prefix evaluated
    for i in range(1, n + 1):
        # Optimization: Look back at most 'longest_word_len' steps
        start_j = max(0, i - longest_word_len)

        for j in range(i - 1, start_j - 1, -1):
            if dp[j] and s[j:i] in dictionary:
                dp[i] = True
                parent_length[i] = i - j  # Track the word length
                break  # Move to next i once a valid split path is established

    # If the entire string cannot be segmented, return an empty list
    if not dp[n]:
        return []

    # Reconstruct the words from back to front
    words = []
    curr = n
    while curr > 0:
        word_len = parent_length[curr]
        words.append(s[curr - word_len:curr])
        curr -= word_len

    # Reverse to restore original sentence word order
    words.reverse()
    return words


if __name__ == "__main__":
    dictionary = {"mobile", "samsung", "sam", "sung",
                  "man", "mango", "icecream", "and",
                  "go", "i", "like", "ice", "cream", "jam",
                  "painting", "paint", "inga", "park", "lake"}
    s = "ilikepaintinga"

    # Outputs: i like paint inga
    print(" ".join(can_string_be_decomposed(s, dictionary)) + " ")
