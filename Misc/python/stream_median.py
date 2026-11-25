"""Running median of a stream using a min-heap and a max-heap."""
import heapq
import random
import sys

MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100


def handle_error():
    print("Test failed")
    sys.exit(1)


def get_median(min_heap, max_heap, cur_value):
    """
    min_heap: holds the larger half of the stream
    max_heap: holds the smaller half (values stored negated for heapq)
    Returns the median after adding cur_value.
    """
    # Larger values (>= smallest of the larger half) go to min_heap
    if not min_heap or cur_value >= min_heap[0]:
        heapq.heappush(min_heap, cur_value)
    else:
        heapq.heappush(max_heap, -cur_value)

    # Rebalance so sizes differ by at most one
    if len(min_heap) > len(max_heap) + 1:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(min_heap) == len(max_heap):
        return (min_heap[0] + (-max_heap[0])) // 2
    if len(min_heap) > len(max_heap):
        return min_heap[0]
    return -max_heap[0]


def print_array(a):
    print("".join(f"{x} " for x in a))


def sort_and_get_median(a):
    b = sorted(a)
    print("Sorted : ", end="")
    print_array(b)
    middle_pos = len(b) // 2
    if len(b) % 2 == 0:
        return (b[middle_pos - 1] + b[middle_pos]) // 2
    return b[middle_pos]


def test():
    min_heap, max_heap = [], []
    length = 1 + random.randrange(MAX_NUM_ELEMS)
    a = [random.randrange(MAX_VALUE) for _ in range(length)]
    for i in range(length):
        # add one element at a time and find the median
        print("Stream : ", end="")
        print_array(a[:i + 1])
        median = get_median(min_heap, max_heap, a[i])
        expected_result = sort_and_get_median(a[:i + 1])
        print(f"Median = {median}")
        if median != expected_result:
            handle_error()
        print("_________________________________________________")


def main():
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")


if __name__ == "__main__":
    main()
