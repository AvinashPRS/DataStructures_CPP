"""Demonstrates using a key function to sort characters in decreasing order of frequency."""
from collections import Counter

if __name__ == "__main__":
    s = "Heellloooo"

    # Counting the frequency of each character in the string
    freq = Counter(s)

    # Sort the string based on character frequency (highest first)
    s = "".join(sorted(s, key=lambda c: freq[c], reverse=True))

    # Display the sorted string based on character frequency
    print(s)
