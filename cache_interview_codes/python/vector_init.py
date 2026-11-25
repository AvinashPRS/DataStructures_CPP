"""
Initialize a vector from an array and compute the median (port of vector_init.cpp).
The median works on a copy, so the original array and vector are unchanged.
"""


def median(seq):
    v = list(seq)  # copy, like `vector<T> v(b, e)`
    size = len(v)
    if size == 0:
        raise ValueError("median of an empty container")

    v.sort()
    mid = size // 2
    return (v[mid] + v[mid - 1]) / 2 if size % 2 == 0 else v[mid]


def fmt(x):
    """print doubles like C++ default cout (e.g. 7.5, 5.8)."""
    return f"{x:g}"


# main code harness:
def main():
    # initialize the array
    double_arr = (7.5, 2.2, 1.5, 6.4, 4.9, 5.8, 9.4)

    # initialize the vector from the array
    double_vec = list(double_arr)

    print("Initial values of the array: " + ", ".join(fmt(x) for x in double_arr))
    print("Initial values of the vector: " + ", ".join(fmt(x) for x in double_vec))

    # print the median values
    print(f"The median value for the array: {fmt(median(double_arr))}")
    print(f"The median value for the vector: {fmt(median(double_vec))}")

    print("Final values of the array: " + ", ".join(fmt(x) for x in double_arr))
    print("Final values of the vector: " + ", ".join(fmt(x) for x in double_vec))


if __name__ == "__main__":
    main()
