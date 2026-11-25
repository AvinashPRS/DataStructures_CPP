"""Word transformation (word ladder) using BFS."""
import string
import sys
from collections import deque


def handle_error():
    print("Test failed ")
    sys.exit(1)


def transform_word(begin_word, end_word, dictionary):
    """
    Returns the list of words from begin_word to end_word changing one
    character at a time using only dictionary words, or None if impossible.
    """
    q = deque([begin_word])
    visited = {begin_word}
    # If we can transform a -> b, we store reverse_path[b] = a
    reverse_path = {}

    while q:
        cur_word = q.popleft()

        if cur_word == end_word:
            result = [cur_word]
            while cur_word in reverse_path:
                cur_word = reverse_path[cur_word]
                result.insert(0, cur_word)
            return result

        # All words obtained by changing a single character
        for i in range(len(cur_word)):
            for c in string.ascii_lowercase:
                new_word = cur_word[:i] + c + cur_word[i + 1:]
                if new_word in dictionary and new_word not in visited:
                    q.append(new_word)
                    visited.add(new_word)
                    reverse_path[new_word] = cur_word

    return None  # transformation is not possible


def test():
    dictionary = {"tall", "bell", "walk", "ball", "talk"}
    result = transform_word("bell", "walk", dictionary)
    if not result:
        handle_error()
    print("".join(f"{w} " for w in result))


def main():
    test()
    print("Test passed ")


if __name__ == "__main__":
    main()
