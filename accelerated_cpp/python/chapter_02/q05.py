# Chapter 2, exercise 5: print a square, a rectangle and a triangle.


def main():
    square_length = 3
    for _ in range(square_length):
        print("*" * square_length)
    print()

    rectangle_width = 4
    rectangle_height = 3
    for _ in range(rectangle_height):
        print("*" * rectangle_width)
    print()

    triangle_height = 3
    for r in range(triangle_height):
        length = r * 2 + 1
        spaces = (triangle_height * 2 - 1 - length) // 2
        print(" " * spaces + "*" * length + " " * spaces)


if __name__ == "__main__":
    main()
