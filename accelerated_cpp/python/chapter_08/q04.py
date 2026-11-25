# Chapter 8, exercise 4: reverse a range in place with swaps.


def reverse(seq, begin=0, end=None):
    if end is None:
        end = len(seq)
    while begin != end:
        end -= 1
        if begin != end:
            seq[begin], seq[end] = seq[end], seq[begin]
            begin += 1


def main():
    numbers = [1, 2, 3, 4, 5]
    reverse(numbers)
    print("Reversed numbers are: " + ", ".join(map(str, numbers)))


if __name__ == "__main__":
    main()
