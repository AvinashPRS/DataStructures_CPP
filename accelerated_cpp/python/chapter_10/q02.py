# Chapter 10, exercise 2: median of any iterable, without changing it.


def median(iterable):
    v = sorted(iterable)  # copy, so the caller's data is untouched
    size = len(v)
    if size == 0:
        raise ValueError("median of an empty container")
    mid = size // 2
    return (v[mid] + v[mid - 1]) / 2 if size % 2 == 0 else v[mid]
