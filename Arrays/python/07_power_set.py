"""
Generate the power set (all subsets) of an array.

Solution 1 (iterative): every integer i in [0, 2^n) is a bitmask selecting a subset.
Solution 2 (recursive): for each position, exclude the element and recurse, then
    include the element and recurse.

    TC: O(n * 2^n)
    SC: O(n)
"""


def subset_str(elements):
    return "{" + "".join(f"{x} " for x in elements) + "}"


def generate_subsets(a):
    """Iterative version using bitmasks."""
    n = len(a)
    for selection in range(1 << n):
        print(subset_str(a[i] for i in range(n) if selection & (1 << i)))


def generate_subsets_r(a, is_selected=None, pos=0):
    """Recursive version."""
    if is_selected is None:
        is_selected = [False] * len(a)

    if pos >= len(a):
        print(subset_str(x for x, sel in zip(a, is_selected) if sel))
        return

    is_selected[pos] = False
    generate_subsets_r(a, is_selected, pos + 1)

    is_selected[pos] = True
    generate_subsets_r(a, is_selected, pos + 1)


def test(a):
    generate_subsets(a)
    print("______________________________\n")


def test_r(a):
    generate_subsets_r(a)
    print("______________________________\n")


if __name__ == "__main__":
    for arr in ([], [0], [0, 1, 2]):
        test(arr)
    for arr in ([], [0], [0, 1, 2]):
        test_r(arr)
    print("Test passed")
