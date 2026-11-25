"""
Word counting with maps (Accelerated C++ style).

Reads words from stdin, counts each word, then groups words by their count
and prints them in increasing order of count (like std::map, keys sorted).

Example:
    echo "a b a c b a" | python3 maps.py
"""
import sys
from collections import Counter


def main():
    # store each word and an associated counter
    counters = Counter(sys.stdin.read().split())

    # group words by how often they occur
    occurrences = {}
    for word in sorted(counters):
        occurrences.setdefault(counters[word], []).append(word)

    for count in sorted(occurrences):
        print(f"words that occur {count} time(s): " + ", ".join(occurrences[count]))


if __name__ == "__main__":
    main()
