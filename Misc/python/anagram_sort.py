"""Sort a list of words so that anagrams appear together."""
import sys


def handle_error():
    print("Test failed ")
    sys.exit(1)


def anagram_sort(word_list):
    """Sorts word_list in place so that anagrams occur together."""
    # helper holds (word with sorted characters, original index)
    helper = [("".join(sorted(w)), i) for i, w in enumerate(word_list)]
    # Sort the helper based on the sorted words (stable on ties like qsort
    # isn't guaranteed to be; we use the index as a tie-breaker)
    helper.sort()
    # Move the words based on the indexes in the helper
    word_list[:] = [word_list[index] for _, index in helper]


def print_words(words):
    print("".join(f"{w} " for w in words))


def test():
    word_list = ["rat", "atm", "hill", "art", "mat", "tar"]
    expected_result = ["atm", "mat", "rat", "art", "tar", "hill"]

    print("Before sorting: ", end="")
    print_words(word_list)
    anagram_sort(word_list)
    print("After  sorting: ", end="")
    print_words(word_list)

    if word_list != expected_result:
        handle_error()


def main():
    test()
    print("Test passed")


if __name__ == "__main__":
    main()
