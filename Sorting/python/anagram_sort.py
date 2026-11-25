"""Group anagrams together in a list of words."""
import sys


def anagram_sort(word_list):
    """Groups anagrams together in the input list (in place)."""
    if len(word_list) <= 1:
        return

    # 1. Build helper pairs of (sorted characters, original index)
    helper = [("".join(sorted(w)), i) for i, w in enumerate(word_list)]

    # 2. Sort the helper by the normalized word using a lambda
    helper.sort(key=lambda h: h[0])

    # 3. Reorder the original word list using a scratchpad
    word_list[:] = [word_list[idx] for _, idx in helper]


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

    # "amt" < "art", so atm/mat come first; the stable sort keeps input order within a group
    if word_list == expected_result:
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)


if __name__ == "__main__":
    test()
