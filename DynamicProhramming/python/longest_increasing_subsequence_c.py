"""Longest increasing subsequence (O(n^2) DP) with reconstruction."""


def find_lis(a):
    """
    a: list in which we need to find the longest increasing sequence. Should have >= 1 element
    Return value: the longest increasing sequence as a list
    """
    n = len(a)
    # seq_length stores length of LIS for each position of a
    # Each element by itself forms a sequence of length 1
    seq_length = [1] * n
    # prev_ix stores the index of previous element in the LIS sequence
    prev_ix = [0] * n

    # Find the LIS for each position in a
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i] and seq_length[i] < seq_length[j] + 1:
                seq_length[i] = seq_length[j] + 1
                prev_ix[i] = j

    # The longest LIS amongst all positions of a will be the LIS for the whole array
    lis_length = 1
    lis_end = 0
    for i in range(1, n):
        if lis_length < seq_length[i]:
            lis_length = seq_length[i]
            lis_end = i

    # Use prev_ix to reconstruct the LIS; lis_end is the index of its last element
    lis = [0] * lis_length
    j = lis_end
    for i in range(lis_length - 1, -1, -1):
        lis[i] = a[j]
        j = prev_ix[j]

    return lis


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def run_test(a):
    print("Input : ", end="")
    print_array(a)
    lis = find_lis(a)
    print("LIS : ", end="")
    print_array(lis)
    print("___________________________________________")


if __name__ == "__main__":
    run_test([6, 3, 2, 4, 5])
    run_test([2, 4, 3, 1, 7, 7, 9])
    print("Test passed")
