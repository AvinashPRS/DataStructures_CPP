# Chapter 8, exercise 2: implement standard-library algorithms by hand.
# Ranges are expressed as (sequence, begin_index, end_index); output
# "iterators" are lists that results are appended to.


def equal(seq1, b, e, seq2, b2):
    while b != e:
        if seq1[b] != seq2[b2]:
            return False
        b += 1
        b2 += 1
    return True


def search(seq, b, e, seq2, b2, e2):
    """Index of the first occurrence of seq2[b2:e2] in seq[b:e], or e."""
    while b != e:
        bi, b2i = b, b2
        while seq[bi] == seq2[b2i]:
            bi += 1
            b2i += 1
            if b2i == e2:
                return b
            if bi == e:
                return e
        b += 1
    return e


def find(seq, b, e, t):
    while b != e:
        if seq[b] == t:
            return b
        b += 1
    return e


def find_if(seq, b, e, p):
    while b != e:
        if p(seq[b]):
            return b
        b += 1
    return e


def copy(seq, b, e, d):
    while b != e:
        d.append(seq[b])
        b += 1
    return d


def remove_copy(seq, b, e, d, t):
    while b != e:
        if seq[b] != t:
            d.append(seq[b])
        b += 1
    return d


def remove_copy_if(seq, b, e, d, p):
    while b != e:
        if not p(seq[b]):
            d.append(seq[b])
        b += 1
    return d


def remove(seq, b, e, t):
    """Move elements not equal to t to the front; return the new end."""
    i = b
    while b != e:
        if seq[b] != t:
            seq[i] = seq[b]
            i += 1
        b += 1
    return i


def transform(seq, b, e, d, f):
    while b != e:
        d.append(f(seq[b]))
        b += 1
    return d


def partition(seq, b, e, p):
    """Reorder so elements satisfying p come first; return the split point."""
    while b != e:
        while p(seq[b]):
            b += 1
            if b == e:
                return b
        while True:
            e -= 1
            if b == e:
                return b
            if p(seq[e]):
                break
        seq[b], seq[e] = seq[e], seq[b]
        b += 1
    return b


def accumulate(seq, b, e, t):
    while b != e:
        t += seq[b]
        b += 1
    return t


def less_than_5(i):
    return i < 5


def main():
    numbers = [6, 2, 9, 8, 1, 3]
    print("The original vector is: " + ", ".join(map(str, numbers)))
    partition(numbers, 0, len(numbers), less_than_5)
    print("The partitioned vector is: " + ", ".join(map(str, numbers)))


if __name__ == "__main__":
    main()
