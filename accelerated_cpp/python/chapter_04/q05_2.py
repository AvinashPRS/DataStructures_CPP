# Chapter 4, exercise 5 (part 2): count how many times each word occurred.
from read_words import read_words


def main():
    print("Enter a sentence, followed by end-of-file: ")
    words = sorted(read_words())
    if not words:
        return

    # walk the sorted list, grouping equal words together
    word = words[0]
    count = 0
    for w in words + [None]:  # sentinel flushes the final group
        if w != word:
            print(f"Word {word} appeared {count} time{'s.' if count > 1 else '.'}")
            word = w
            count = 1
        else:
            count += 1


if __name__ == "__main__":
    main()
