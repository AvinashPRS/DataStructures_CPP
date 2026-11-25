"""
Generic in-place reverse using bidirectional "iterators" (port of reverse_iter.cpp).
Indices begin/end play the role of the C++ bidirectional iterators.
"""


def reverse(seq, begin, end):
    while begin != end:
        end -= 1
        if begin != end:
            seq[begin], seq[end] = seq[end], seq[begin]
            begin += 1


# main code harness:
def main():
    numbers = []
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    reverse(numbers, 0, len(numbers))

    print("Reversed numbers are: " + ", ".join(str(n) for n in numbers))


if __name__ == "__main__":
    main()
