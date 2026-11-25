"""Sort a list of words so that anagrams occur together (explicit helper-array version)."""
import sys
from dataclasses import dataclass


def handle_error():
    print("Test failed ")
    sys.exit(1)


@dataclass
class AnagramHelper:
    word: str   # word with its characters sorted
    index: int  # original index of the word


def print_helper(helper):
    print("".join(f"[ {h.word} , {h.index}] " for h in helper))


def sort_word(word):
    """Sorts the characters in a string."""
    return "".join(sorted(word))


def anagram_sort(word_list):
    """
    word_list: list of words, re-ordered in place so that anagrams occur together
    """
    # Build helper entries: normalized word + original index
    helper = [AnagramHelper(sort_word(w), i) for i, w in enumerate(word_list)]

    # Sort all the words in the helper
    helper.sort(key=lambda h: h.word)

    # Reorder using a scratchpad
    scratchpad = [word_list[h.index] for h in helper]
    word_list[:] = scratchpad


def print_words(words):
    print("".join(f"{w} " for w in words))


def test():
    word_list = ["rat", "atm", "hill", "art", "mat", "tar"]
    # "art"/"rat"/"tar" -> "art", "atm"/"mat" -> "amt", "hill" -> "hill"
    expected_result = ["art", "rat", "tar", "atm", "mat", "hill"]

    print("Before sorting: ", end="")
    print_words(word_list)

    anagram_sort(word_list)

    print("After  sorting: ", end="")
    print_words(word_list)

    # NOTE: the C version uses qsort (unstable); Python's sort is stable, so ties
    # keep their original order. Compare by anagram group to be order-agnostic.
    if [sort_word(w) for w in word_list] != [sort_word(w) for w in expected_result] \
            or sorted(word_list) != sorted(expected_result):
        handle_error()


if __name__ == "__main__":
    test()
    print("Test passed")
