"""Box stacking: maximum height of a stack of boxes (unlimited instances, any rotation)."""
import sys
from dataclasses import dataclass


@dataclass
class Box:
    height: int
    length: int
    breadth: int


def handle_error():
    print("Test failed ")
    sys.exit(1)


def max_stack_height(a):
    """
    a: list of boxes of different dimensions. Should contain atleast one box
    Result: maximum height of the stack of boxes that can be constructed.
    Assumption is that multiple instances of each box are available
    """
    # For each box, all 3 orientations are possible. Length is always >= breadth
    boxes = []
    for b in a:
        boxes.append(Box(b.height, max(b.length, b.breadth), min(b.length, b.breadth)))
        boxes.append(Box(b.length, max(b.breadth, b.height), min(b.breadth, b.height)))
        boxes.append(Box(b.breadth, max(b.length, b.height), min(b.length, b.height)))

    # Sort the boxes so that the boxes with larger base area appear first
    boxes.sort(key=lambda box: box.length * box.breadth, reverse=True)

    num_boxes = len(boxes)
    best_height = [box.height for box in boxes]

    # Iterate through all boxes and find the best height for each box
    for i in range(1, num_boxes):
        for j in range(i):
            # We can place box i on box j only if base of box i is smaller than base of box j
            if boxes[i].length < boxes[j].length and boxes[i].breadth < boxes[j].breadth:
                if best_height[i] < best_height[j] + boxes[i].height:
                    best_height[i] = best_height[j] + boxes[i].height

    # Find the stack with the maximum height
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
