# Chapter 3, exercise 4: report the lengths of the shortest and longest words.
import sys


def main():
    print("Enter a sentence, followed by end-of-file: ")
    sizes = sorted(len(word) for word in sys.stdin.read().split())
    if not sizes:
        return
    print(f"Shortest length: {sizes[0]}")
    print(f"Longest length: {sizes[-1]}")


if __name__ == "__main__":
    main()
