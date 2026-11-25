# Chapter 7, exercise 1: group words by how often they occur.
import sys
from collections import Counter


def main():
    counters = Counter(sys.stdin.read().split())

    occurrences = {}
    for word in sorted(counters):
        occurrences.setdefault(counters[word], []).append(word)

    for count in sorted(occurrences):
        print(f"words that occur {count} time(s): " + ", ".join(occurrences[count]))


if __name__ == "__main__":
    main()
