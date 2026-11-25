"""
Generic K&R-style quicksort that takes a comparison function
(Python version of quicksortK&R.c, which used void* and a function pointer).
"""


def swap(v, i, j):
    v[i], v[j] = v[j], v[i]


def qsort_generic(v, left, right, comp):
    """Sort v[left]..v[right] into increasing order using comp(a, b) -> <0, 0, >0."""
    if left >= right:
        return

    swap(v, left, (left + right) // 2)
    last = left
    for i in range(left + 1, right + 1):
        # Call the comparison function to compare arbitrary objects generically
        if comp(v[i], v[left]) < 0:
            last += 1
            swap(v, last, i)

    swap(v, left, last)
    qsort_generic(v, left, last - 1, comp)
    qsort_generic(v, last + 1, right, comp)


def strcmp(a, b):
    """Python equivalent of C's strcmp."""
    return (a > b) - (a < b)


if __name__ == "__main__":
    planets = ["Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune"]

    print("Original array:")
    print(" ".join(planets))
    print()

    # Pass strcmp as the comparison function (like a function pointer in C)
    qsort_generic(planets, 0, len(planets) - 1, strcmp)

    print("Lexicographically sorted array:")
    print(" ".join(planets))
