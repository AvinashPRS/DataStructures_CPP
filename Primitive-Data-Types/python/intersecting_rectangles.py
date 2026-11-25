"""
Problem:
    Given information about two axis parallel rectangles, find whether these two rectangles intersect or not.
    If they intersect, then give information about the shared area.

Input Rectangle data:
    Coordinate of the lower left end, height and length of the rectangle.

Output:
    (intersection?, lower end point of shared rectangular area, length, height)
    if intersection is there: 1 else 0
    Others: real nos. if intersection is there, else -1
"""
from dataclasses import dataclass


@dataclass
class Rectangle:
    # lower end point, length and height
    x: int
    y: int
    length: int
    height: int


def create_rectangle(x, y, length, height):
    """For creating a rectangle object"""
    return Rectangle(x, y, length, height)


def does_rectangles_intersect(r1, r2):
    """
    Checks if the two rectangles intersect or not
    Output:
    (intersection, x, y, length, height)
    """
    # see whether the two rectangles intersect
    # If two rectangles share area then some part of their length and width will be common
    intersect = (r1.x <= r2.x + r2.length and r2.x <= r1.x + r1.length and
                 r1.y <= r2.y + r2.height and r2.y <= r1.y + r1.height)

    if intersect:
        return [
            1, max(r1.x, r2.x), max(r1.y, r2.y),
            min(r1.x + r1.length, r2.x + r2.length) - max(r1.x, r2.x),
            min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y),
        ]

    return [0, -1, -1, -1, -1]


if __name__ == "__main__":
    r1 = create_rectangle(76, 9, 12, 14)
    r2 = create_rectangle(20, 1, 62, 60)

    result = does_rectangles_intersect(r1, r2)
    print(" ".join(map(str, result)))
