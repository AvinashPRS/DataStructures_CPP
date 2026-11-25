"""Area of the largest rectangle in a histogram (stack based)."""
import sys


def handle_error():
    print("Test failed ")
    sys.exit(1)


def print_array(a):
    print("".join(f"{x} " for x in a))


def find_max_area(histo_height):
    """
    histo_height[i] has height of ith bar (n >= 1).
    Returns the area of the largest rectangle in the histogram.
    """
    n = len(histo_height)
    max_area = 0
    height_stack = []  # heights of the bars
    index_stack = []   # indices of the bars
    popped_index = 0

    for i in range(n):
        if not height_stack or histo_height[i] > height_stack[-1]:
            # push height and index of current bar
            height_stack.append(histo_height[i])
            index_stack.append(i)
        elif histo_height[i] < height_stack[-1]:
            while height_stack and histo_height[i] < height_stack[-1]:
                popped_index = index_stack.pop()
                popped_height = height_stack.pop()
                # area from popped bar to the current bar
                area = popped_height * (i - popped_index)
                max_area = max(max_area, area)
            # push height of the current bar
            height_stack.append(histo_height[i])
            # push the LAST POPPED INDEX, since we can form a rectangle from
            # it to the current bar with the current bar's height
            index_stack.append(popped_index)

    # Process the remaining elements in the stacks
    while height_stack:
        popped_index = index_stack.pop()
        area = height_stack.pop() * (n - popped_index)
        max_area = max(max_area, area)
    return max_area


def run_test(histo_height, expected):
    max_area = find_max_area(histo_height)
    print("Histogram: ", end="")
    print_array(histo_height)
    print(f"Max area = {max_area}")
    if max_area != expected:
        handle_error()
    print("____________________________________")


def main():
    run_test([3, 2, 5, 6, 1, 4, 4], 10)
    run_test([2, 4, 2, 1], 6)
    print("Test passed ")


if __name__ == "__main__":
    main()
