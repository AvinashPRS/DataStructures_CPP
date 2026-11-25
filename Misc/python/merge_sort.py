"""
Merge sort. See https://en.wikipedia.org/wiki/Merge_sort
YouTube lesson (C version): https://www.youtube.com/watch?v=LeWuki7AQLo

Example visualisation:

         [38, 27, 43, 3, 9, 82, 10]
                    /   \\
      [38, 27, 43, 3]   [9, 82, 10]
       /         |         |      \\
  [38, 27]    [43, 3]   [9, 82]   [10]
   /   |      /    |    /    \\      |
[38]  [27]  [43]  [3]  [9]   [82]  [10]
   \\  /       \\   /     \\     /     |
  [27, 38]    [3, 43]   [9, 82]    [10]
      \\         /          \\        /
    [3, 27, 38, 43]        [9, 10, 82]
          \\                  /
         [3, 9, 10, 27, 38, 43, 82]

The array is broken into progressively smaller portions until they hold one
element (sorted by definition); then the sorted portions are merged.
"""


def merge_sort(a):
    """Convenience wrapper: sort the entire list a in place."""
    merge_sort_recursion(a, 0, len(a) - 1)


def merge_sort_recursion(a, l, r):
    """Divide-and-conquer step on a[l..r]."""
    if l < r:
        m = l + (r - l) // 2
        merge_sort_recursion(a, l, m)
        merge_sort_recursion(a, m + 1, r)
        merge_sorted_arrays(a, l, m, r)


def merge_sorted_arrays(a, l, m, r):
    """Merge the sorted portions a[l..m] and a[m+1..r]."""
    temp_left = a[l:m + 1]
    temp_right = a[m + 1:r + 1]
    left_length, right_length = len(temp_left), len(temp_right)
    i = j = 0
    for k in range(l, r + 1):
        # take from the left while it has elements and its head is smaller
        # (or the right side is exhausted)
        if i < left_length and (j >= right_length or temp_left[i] <= temp_right[j]):
            a[k] = temp_left[i]
            i += 1
        else:
            a[k] = temp_right[j]
            j += 1


def main():
    array = [9, 4, 8, 1, 7, 0, 3, 2, 5, 6]
    merge_sort(array)
    print("".join(f"{x} " for x in array))


if __name__ == "__main__":
    main()
