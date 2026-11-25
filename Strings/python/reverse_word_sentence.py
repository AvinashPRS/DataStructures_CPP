"""
Problem:
    Given a string sentence, reverse all the words in the sentence
    E.g: Coding and gaming ---> gaming and Coding

Input:
    sentence: string

Output:
    resultant string
TC: O(n), n: no. of chars.
"""


def reverse_words_sentence(sentence):
    """
    First reverse the individual words and then reverse the entire string
    """
    # reverse the individual words, then the entire string
    reversed_words = " ".join(word[::-1] for word in sentence.split(" "))
    return reversed_words[::-1]


if __name__ == "__main__":
    print(reverse_words_sentence("Coding and gaming"))
    print(reverse_words_sentence("Anna likes Bob"))
