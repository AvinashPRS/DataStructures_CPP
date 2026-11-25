# Chapter 6, exercise 9: concatenate all elements of a list of strings.
from functools import reduce
import operator


def main():
    words = ["hello ", "my ", "name ", "is ", "Altug"]
    concatenated_words = reduce(operator.add, words, "")
    print("The result of concatenation is: " + concatenated_words)


if __name__ == "__main__":
    main()
