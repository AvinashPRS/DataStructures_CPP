# Chapter 4, exercise 5 (part 1): count the number of words in the input.
from read_words import read_words


def main():
    print("Enter a sentence, followed by end-of-file: ")
    words = read_words()
    print(f"There are {len(words)} words in the input.")


if __name__ == "__main__":
    main()
