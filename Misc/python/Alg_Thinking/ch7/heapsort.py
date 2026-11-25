"""Heapsort using a 1-indexed binary min-heap."""

N = 10


def min_heap_insert(heap, value):
    """heap[0] is unused; len(heap) - 1 is the number of elements."""
    heap.append(value)
    i = len(heap) - 1
    while i > 1 and heap[i] < heap[i // 2]:
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i //= 2


def min_heap_extract(heap):
    remove = heap[1]
    heap[1] = heap[-1]
    heap.pop()
    num_heap = len(heap) - 1
    i = 1
    while i * 2 <= num_heap:
        child = i * 2
        if child < num_heap and heap[child + 1] < heap[child]:
            child += 1
        if heap[child] < heap[i]:
            heap[i], heap[child] = heap[child], heap[i]
            i = child
        else:
            break
    return remove


def main():
    values = [96, 61, 36, 74, 45, 60, 47, 6, 95, 93]
    min_heap = [None]

    # Heapsort. 4 lines!
    for v in values:
        min_heap_insert(min_heap, v)
    for i in range(N):
        values[i] = min_heap_extract(min_heap)

    print("".join(f"{v} " for v in values))


if __name__ == "__main__":
    main()
