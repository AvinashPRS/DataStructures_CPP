"""
String decomposition: given a sentence string and a list of words (all the same length),
find every starting index in the sentence where a concatenation of all the words, in any
order, appears.

Input: sentence string and list of words
Output: list of int

Solution:
    For each index in the sentence, check the substring starting there:
    The words are of equal length m, so take the next m characters, check it is one of the
    words (and not used more times than it appears in the list), and continue for the
    remaining words. If all words are matched, record the index.

    TC: O(Nnm), N: no. of chars in sentence, n: no. of words, m: length of each word
    SC: O(n)
"""
from collections import Counter


def does_sentence_contain_words(sentence, start, word_freq, words):
    freq = Counter()
    word_len = len(words[0])

    for i in range(len(words)):
        curr_word = sentence[start + i * word_len: start + (i + 1) * word_len]

        # the word doesn't match: concatenation not possible here
        if curr_word not in word_freq:
            return False

        freq[curr_word] += 1
        # a valid word appearing more times than required blocks another word
        if freq[curr_word] > word_freq[curr_word]:
            return False
    return True


def string_decomposition_possible(sentence, words):
    if not words:
        return []
    word_freq = Counter(words)
    total_len = len(words[0]) * len(words)

    return [i for i in range(len(sentence) - total_len + 1)
            if does_sentence_contain_words(sentence, i, word_freq, words)]


if __name__ == "__main__":
    sentence = "amanaplanacanal"
    words = ["can", "apl", "ana"]
    print(" ".join(str(r) for r in string_decomposition_possible(sentence, words)))
