"""Find the running median of a stream using a min-heap and a max-heap."""
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
    min_heap: heapq list storing the larger half of numbers in the stream
    max_heap: heapq list storing the smaller half of numbers in the stream
              (values are stored negated so heapq behaves as a max-heap)
    cur_value: value of the current item in the stream
    Returns: median of the stream
    """
    # If min_heap is empty, add the current value to min_heap.
    # If min_heap is non-empty, the top of min_heap will contain the smallest
    # among the larger half of numbers in the stream. So if current value is
    # larger than the top of min_heap, then add it to min_heap otherwise add
    # it to max_heap
    if not min_heap or cur_value >= min_heap[0]:
        heapq.heappush(min_heap, cur_value)
    else:
        heapq.heappush(max_heap, -cur_value)

    # If one heap has more than 1 element than the other, move its top
    # into the other heap
    if len(min_heap) > len(max_heap) + 1:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # If both heaps are of the same size, then the median will be the
    # average of the top element in the two heaps. Otherwise the median is
    # the top of the heap with more elements
    if len(min_heap) == len(max_heap):
        median = int((min_heap[0] + -max_heap[0]) / 2)  # truncate like C++
    elif len(min_heap) > len(max_heap):
        median = min_heap[0]
    else:
        median = -max_heap[0]

    return median


def print_array(a):
    print("".join(f"{x} " for x in a))


def sort_and_get_median(a):
    # Copy so that we don't change the contents of a
    b = sorted(a)

    print("Sorted : ", end="")
    print_array(b)

    middle_pos = len(b) // 2

    if len(b) % 2 == 0:
        return int((b[middle_pos - 1] + b[middle_pos]) / 2)
    return b[middle_pos]


def generate_array(length):
    return [random.randrange(MAX_VALUE) for _ in range(length)]


def test():
    min_heap = []
    max_heap = []

    # Randomly pick the number of elements
    length = 1 + random.randrange(MAX_NUM_ELEMS)

    # Generate numbers in the array
    a = generate_array(length)

    for i in range(length):
        # Go on adding one element at a time and finding the median
        print("Stream : ", end="")
        print_array(a[:i + 1])

        # Find the median using the efficient technique
        median = get_median(min_heap, max_heap, a[i])

        # Find the median using sorting
        expected_result = sort_and_get_median(a[:i + 1])

        print(f"Median = {median}")

        if median != expected_result:
            handle_error()

        print("_________________________________________________")


if __name__ == "__main__":
    for _ in range(MAX_NUM_TESTS):
        test()
    print("Test passed")
