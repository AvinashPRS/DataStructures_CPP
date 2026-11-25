"""Sort an almost-sorted array (each element at most k positions away) using a min heap."""
import heapq
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100


def handle_error():
    print("Test failed")
    sys.exit(1)


def sort_almost_sorted_array(a, k):
    """
    a: almost sorted list that should be fully sorted (in place)
    k: max distance any element should be moved so that the list becomes sorted
    """
    length = len(a)
    min_heap = []

    # Fill in the first k values into the min_heap (or all of them if length < k)
    read_pos = 0
    while read_pos < min(k, length):
        heapq.heappush(min_heap, a[read_pos])
        read_pos += 1

    # Push a[read_pos] then pop the smallest value back into the write position
    write_pos = 0
    while read_pos < length:
        a[write_pos] = heapq.heappushpop(min_heap, a[read_pos])
        read_pos += 1
        write_pos += 1

    # Pop out the remaining elements in the heap
    while min_heap:
        a[write_pos] = heapq.heappop(min_heap)
        write_pos += 1


def print_array(a):
    print("".join(f"{x} " for x in a))


def generate_array(length, k):
    """Generate a list where no element is more than k positions from its sorted place."""
    a = sorted(random.randrange(MAX_VALUE) for _ in range(length))

    # Divide the array into regions of size k and do k random swaps in each region
    max_num_regions = (length + k - 1) // k
    for region_nr in range(max_num_regions):
        for _ in range(k):
            index1 = region_nr * k + random.randrange(k)
            index2 = region_nr * k + random.randrange(k)
            if index1 < length and index2 < length:
                a[index1], a[index2] = a[index2], a[index1]
    return a


def test():
    length = 1 + random.randrange(MAX_NUM_ELEMS)
    k = 1 + random.randrange(length)

    a = generate_array(length, k)

    print(f"K = {k}")
    print("Input  : ", end="")
    print_array(a)

    b = list(a)

    sort_almost_sorted_array(a, k)

    print("Output : ", end="")
    print_array(a)

    b.sort()
    if a != b:
        handle_error()

    print("_________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
