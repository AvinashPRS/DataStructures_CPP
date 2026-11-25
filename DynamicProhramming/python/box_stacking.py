"""Box stacking: maximum height of a stack of boxes (unlimited instances, any rotation)."""
import sys
from dataclasses import dataclass


def handle_error():
    print("Test failed ")
    sys.exit(1)


@dataclass
class Box:
    height: int
    length: int
    breadth: int


def max_stack_height(a):
    """
    a: list of boxes of different dimensions
    Result: maximum height of the stack of boxes that can be constructed.
    Assumption is that multiple instances of each box are available
    """
    if not a:
        return 0

    # For each box, all 3 orientations are possible. Length will always be >= breadth
    boxes = []
    for box in a:
        boxes.append(Box(box.height, max(box.length, box.breadth), min(box.length, box.breadth)))
        boxes.append(Box(box.length, max(box.breadth, box.height), min(box.breadth, box.height)))
        boxes.append(Box(box.breadth, max(box.length, box.height), min(box.length, box.height)))

    # Higher area boxes should be stored first after sorting
    boxes.sort(key=lambda b: b.length * b.breadth, reverse=True)

    best_height = [b.height for b in boxes]

    # Iterate through all boxes and find the best height for each box
    for i in range(1, len(boxes)):
        for j in range(i):
            # We can place box i on box j only if base of box i is smaller than base of box j
            if boxes[i].length < boxes[j].length and boxes[i].breadth < boxes[j].breadth:
                if best_height[i] < best_height[j] + boxes[i].height:
                    best_height[i] = best_height[j] + boxes[i].height

    # Return the maximum height of the stack
    return max(best_height)


def test_01():
    a = [Box(100, 120, 320), Box(10, 20, 30), Box(40, 60, 70), Box(40, 50, 60)]
    result = max_stack_height(a)
    print(f"Max stack height = {result} ")
    if result != 600:
        handle_error()


def test_02():
    a = [Box(10, 20, 30)]
    result = max_stack_height(a)
    print(f"Max stack height = {result} ")


if __name__ == "__main__":
    test_01()
    test_02()
    print("Test passed ")
