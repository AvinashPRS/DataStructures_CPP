# Chapter 3, exercise 3: count how many times each distinct word appears.
import sys


def main():
    print("Enter a sentence, followed by end-of-file: ")
    words = []
    counts = []
    for word in sys.stdin.read().split():
        if word in words:
            counts[words.index(word)] += 1
        else:
            words.append(word)
            counts.append(1)

    for word, count in zip(words, counts):
        print(f"Word: {word}, Count: {count}")


if __name__ == "__main__":
    main()
