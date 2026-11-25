"""Python equivalents of a few C++ STL algorithms: unique, copy, unique_copy, transform."""
import operator
from itertools import groupby


if __name__ == "__main__":
    # std::sort + std::unique + erase  ->  sorted(set(...))
    vec = [1, 2, 2, 3, 1, 3, 3, 4]
    vec = sorted(set(vec))
    print(*vec)  # 1 2 3 4

    # std::copy with back_inserter  ->  extend / list()
    source = [10, 20, 30]
    dest = []
    dest.extend(source)
    print(*dest)  # 10 20 30

    # std::unique_copy (consecutive duplicates only)  ->  itertools.groupby
    source = [1, 1, 2, 3, 3, 1]
    dest = [k for k, _ in groupby(source)]
    print(*dest)  # 1 2 3 1 (final 1 stays: not consecutive to the first 1s)

    # std::transform is a "map" operation.
    # In-place uppercase of a string (strings are immutable, so rebind)
    text = "hello world"
    text = text.upper()
    print(text)

    # Transform into a new container
    numbers = [1, 2, 3, 4, 5]
    squared = [x * x for x in numbers]     # or list(map(lambda x: x * x, numbers))
    print(*squared)

    # Binary transform: pair vec1[i] and vec2[i] and add them (std::plus)
    vec1 = [1, 2, 3, 4]
    vec2 = [10, 20, 30, 40]
    results = list(map(operator.add, vec1, vec2))
    print(*results)
