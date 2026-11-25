"""
Generic split: the C++ version wrote words to any output iterator.
The Python equivalent is a generator, which can feed a list, a deque,
or be streamed directly to standard output.
"""
from collections import deque


def split(text):
    """Yields whitespace separated words of text"""
    i = 0
    n = len(text)

    while i != n:
        # Advance past leading whitespace
        while i != n and text[i].isspace():
            i += 1

        # Find the end of the current word
        j = i
        while j != n and not text[j].isspace():
            j += 1

        # If a word was found, yield it
        if i != n:
            yield text[i:j]

        i = j


if __name__ == "__main__":
    sample = "Generic functions decouple algorithms from containers"

    # 1. Collect words into a list
    vec_words = list(split(sample))

    # 2. Collect words into a deque (linked-list like container)
    list_words = deque(split(sample))

    # 3. Stream words directly to standard output
    print("Words streamed directly:")
    for word in split(sample):
        print(word)
