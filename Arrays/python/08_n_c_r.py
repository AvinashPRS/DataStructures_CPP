"""
Generate all combinations of r elements from n elements (nCr).

Solution:
    Recursively, for each position either exclude the element or include it,
    stopping as soon as r elements are selected.

    TC: O(n * nCr)
    SC: O(n)
"""


def generate_combinations(a, is_selected, pos, subset_size, cur_num_selections):
    """
    a: input list
    is_selected: is_selected[i] is True if a[i] is in the current subset
    pos: current position in the input
    subset_size: number of elements in the final subset
    cur_num_selections: number of elements selected so far
    """
    if cur_num_selections == subset_size:
        chosen = [x for x, sel in zip(a, is_selected) if sel][:subset_size]
        print("{" + "".join(f"{x} " for x in chosen) + "}")
        return

    if pos >= len(a):
        return

    # Exclude the item from the subset
    is_selected[pos] = False
    generate_combinations(a, is_selected, pos + 1, subset_size, cur_num_selections)

    # Include the item in the subset
    is_selected[pos] = True
    generate_combinations(a, is_selected, pos + 1, subset_size, cur_num_selections + 1)
    is_selected[pos] = False


def test(a, subset_size):
    print("Number of elements in subset =", subset_size)
    generate_combinations(a, [False] * len(a), 0, subset_size, 0)
    print("______________________________\n")


if __name__ == "__main__":
    array1 = [0, 1, 2, 3, 4]
    # Compute 5C0 to 5C5
    for subset_size in range(len(array1) + 1):
        test(array1, subset_size)
    print("Test passed")
