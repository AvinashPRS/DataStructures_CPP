# Chapter 8, exercise 3: median over any random-access range.


def median(seq, b=0, e=None):
    if e is None:
        e = len(seq)
    size = e - b
    if size == 0:
        raise ValueError("median of an empty container")
    seq[b:e] = sorted(seq[b:e])
    mid = b + size // 2
    return (seq[mid] + seq[mid - 1]) / 2.0 if size % 2 == 0 else seq[mid]


def main():
    vec = [1, 7, 8, 2, 5, 4]
    print(f"median is {median(vec):g}")


if __name__ == "__main__":
    main()
