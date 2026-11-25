"""Exercise 1-13: histogram of the lengths of words (horizontal and vertical)."""
import sys

BUFFER = 100


def main():
    histogram = [0] * BUFFER
    histogram_length = 0
    max_word_count = 0

    # Count the words length and store in the histogram at the specific index
    word_count_index = 0
    text = sys.stdin.read()
    for c in list(text) + [None]:  # None marks EOF
        if c is None or c in (" ", "\t", "\n"):
            if word_count_index > 0:
                histogram[word_count_index - 1] += 1
                max_word_count = max(max_word_count,
                                     histogram[word_count_index - 1])
                histogram_length = max(histogram_length, word_count_index - 1)
                word_count_index = 0
        else:
            word_count_index += 1

    # Only keep the useful part of the histogram
    histogram = histogram[:histogram_length + 1]

    print()

    # Print horizontal histogram
    print("Horizontal Histogram\n--------------------")
    for column_index, count in enumerate(histogram):
        print("%3d: \t%s" % (column_index + 1, "#" * count))

    print()

    # Print a vertical histogram
    print("Vertical Histogram\n------------------")
    for line_index in range(max_word_count, -1, -1):
        row = []
        for column_index, count in enumerate(histogram):
            if line_index == 0:
                row.append("%2d " % (column_index + 1))
            elif count >= line_index:
                row.append("## ")
            else:
                row.append("   ")
        print("".join(row))


if __name__ == "__main__":
    main()
