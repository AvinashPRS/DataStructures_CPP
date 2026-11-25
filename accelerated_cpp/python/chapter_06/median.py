# Code taken from §4.1.1/53: compute the median of a list of numbers.


def median(vec):
    size = len(vec)
    if size == 0:
        raise ValueError("median of an empty vector")
    vec = sorted(vec)
    mid = size // 2
    return (vec[mid] + vec[mid - 1]) / 2 if size % 2 == 0 else vec[mid]
