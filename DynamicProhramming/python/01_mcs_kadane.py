"""Maximum continuous sum (Kadane's algorithm), verified against brute force."""
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_ELEMENT_VALUE = 100


def handle_error():
    print("Error occured ")
    sys.exit(1)


def kadane_mcs(a):
    """
    a: list of numbers for which the MCS should be found. Should have >= 1 element
    Return value: (maximum continuous sum, mcs_start_pos, mcs_end_pos)
    """
    mcs_start_pos = mcs_end_pos = 0
    cur_start_pos = 0  # store the start position of the current window

    max_local = max_global = a[0]

    # Traverse from the second element onwards
    for i in range(1, len(a)):
        max_local = max(a[i], a[i] + max_local)
        if max_local == a[i]:
            cur_start_pos = i  # start a new window here

        # Find the global maximum
        if max_local > max_global:
            max_global = max_local
            mcs_start_pos = cur_start_pos
            mcs_end_pos = i

    return max_global, mcs_start_pos, mcs_end_pos


def find_brute_force_mcs(a):
    mcs = float("-inf")
    for start_elem in range(len(a)):
        cur_sum = 0
        for i in range(start_elem, len(a)):
            cur_sum += a[i]
            if mcs < cur_sum:
                mcs = cur_sum
    return mcs


def print_array(a):
    print(" ".join(str(x) for x in a) + " ")


def main():
    for _ in range(MAX_NUM_TESTS):
        # Pick a random number of elements
        num_elems = 1 + random.randrange(MAX_NUM_ELEMS)

        # Generate random values; some elements will be negative
        a = []
        for _ in range(num_elems):
            val = random.randrange(MAX_ELEMENT_VALUE)
            if random.randrange(2) == 0:
                val = -val
            a.append(val)

        print("Input : ", end="")
        print_array(a)

        # Find the maximum continuous sum
        algo_mcs, mcs_start_pos, mcs_end_pos = kadane_mcs(a)

        print(f"Max Continuous Sum = {algo_mcs}, MCS start position = {mcs_start_pos}, "
              f"MCS end position = {mcs_end_pos}")

        verify_sum = sum(a[mcs_start_pos:mcs_end_pos + 1])
        if verify_sum != algo_mcs:
            handle_error()

        # Find the maximum continuous sum using brute force; the two results should match
        if algo_mcs != find_brute_force_mcs(a):
            handle_error()

        print("______________________________________________")

    print("Test passed")


if __name__ == "__main__":
    main()
