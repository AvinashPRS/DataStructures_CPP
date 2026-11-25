"""
Word segmentation problem:
    Given a dictionary of words and a string. Check if the string can be
    decomposed in terms of dictionary words.

    Input: set of strings, single string
    Output: list of decomposed words
Solution:
    We use a 1d array storing the length of the word ending at that index. Initially every entry is -1.
    We start traversal through the given string and for each i < n,
    we check if the word formed by (0, i) is in the dict or not.
    If it is there, then goto next index
    else:
        go back and find the last indices where a dict word ended, from there
        start checking if a word can be formed by (k, i), k < i.
        We can do one optimisation here, instead of going back all the way back to index 0,
        we can find the length of longest word and if the length is W.
        Then we start searching from W indices back only, using this approach makes O(W^2)
    TC: O(n^3) normal way, O(nW^2) if longest word length is found in advance
    SC: O(n), n: length of string
"""


def longest_dict_word_length(dictionary):
    """finds the longest length of dict word"""
    return max((len(word) for word in dictionary), default=0)


def can_string_be_decomposed(s, dictionary):
    """checks if a string can be decomposed in terms of given dictionary words"""
    if not s:
        return []

    # each entry stores the length of the word ending at that index
    word_ending_length = [-1] * len(s)

    # get the length of longest word
    longest_word_len = longest_dict_word_length(dictionary)

    # traverse through the string and keep checking if the substring is a dict string
    for i in range(len(s)):
        # if the current substring exists in dict
        if s[:i + 1] in dictionary:
            word_ending_length[i] = i + 1

        # if there is no substring(0, i) that is a valid word, then check if there
        # is any starting point after 0 from where a valid word can be formed
        if word_ending_length[i] == -1:
            # TC: O(W^2); if there really is a word, then at max it can be
            # longest_word_len back from 'i'
            for j in range(max(i - longest_word_len, 0), i):
                # if a word is found
                if word_ending_length[j] != -1 and s[j + 1:i + 1] in dictionary:
                    word_ending_length[i] = i - j
                    break

    # if the last entry is -1, no word was found till last index,
    # so the string is not decomposable
    if word_ending_length[-1] == -1:
        return []

    # get the individual words from string (in reverse order)
    words = []
    word_idx = len(s) - 1
    while word_idx >= 0:
        length = word_ending_length[word_idx]
        words.append(s[word_idx + 1 - length:word_idx + 1])
        word_idx -= length

    return words


if __name__ == "__main__":
    dictionary = {"mobile", "samsung", "sam", "sung",
                  "man", "mango", "icecream", "and",
                  "go", "i", "like", "ice", "cream", "jam",
                  "painting", "paint", "inga", "park", "lake"}
    s = "ilikepaintinga"

    print(" ".join(can_string_be_decomposed(s, dictionary)) + " ")
