# median for a Vec (or any iterable) of numbers (§4.1.1/53).


def median(vec):
    v = sorted(vec)
    size = len(v)
    if size == 0:
        raise ValueError("median of an empty vector")
    mid = size // 2
    return (v[mid] + v[mid - 1]) / 2 if size % 2 == 0 else v[mid]
