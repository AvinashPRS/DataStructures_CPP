"""Supermarket Promotion: a max-heap and a min-heap of receipts."""
import sys


def heap_insert(heap, receipt_index, cost, better):
    """1-indexed binary heap of (receipt_index, cost); `better(a, b)` is True
    when cost a should be above cost b."""
    heap.append((receipt_index, cost))
    i = len(heap) - 1
    while i > 1 and better(heap[i][1], heap[i // 2][1]):
        heap[i], heap[i // 2] = heap[i // 2], heap[i]
        i //= 2


def heap_extract(heap, better):
    remove = heap[1]
    heap[1] = heap[-1]
    heap.pop()
    num_heap = len(heap) - 1
    i = 1
    while i * 2 <= num_heap:
        child = i * 2
        if child < num_heap and better(heap[child + 1][1], heap[child][1]):
            child += 1
        if better(heap[child][1], heap[i][1]):
            heap[i], heap[child] = heap[child], heap[i]
            i = child
        else:
            break
    return remove


def greater(a, b):
    return a > b


def less(a, b):
    return a < b


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    num_days = data[0]
    pos = 1
    used = []
    max_heap = [None]
    min_heap = [None]
    receipt_index = 0
    total_prizes = 0
    for _ in range(num_days):
        receipts_today = data[pos]
        pos += 1
        for cost in data[pos:pos + receipts_today]:
            heap_insert(max_heap, receipt_index, cost, greater)
            heap_insert(min_heap, receipt_index, cost, less)
            used.append(False)
            receipt_index += 1
        pos += receipts_today

        max_element = heap_extract(max_heap, greater)
        while used[max_element[0]]:
            max_element = heap_extract(max_heap, greater)
        used[max_element[0]] = True

        min_element = heap_extract(min_heap, less)
        while used[min_element[0]]:
            min_element = heap_extract(min_heap, less)
        used[min_element[0]] = True
        total_prizes += max_element[1] - min_element[1]
    print(total_prizes)


if __name__ == "__main__":
    main()
