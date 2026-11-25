# Chapter 5, exercise 5: center the lines of a framed picture.
from split import split


def center(picture):
    centered = list(picture)
    # the picture is assumed to be rectangular
    width = len(centered[0]) - 2
    for idx in range(1, len(centered) - 1):
        # drop the border characters and re-join the words
        unpadded_line = " ".join(split(centered[idx][1:-1]))
        left_padding = (width - len(unpadded_line)) // 2
        right_padding = width - len(unpadded_line) - left_padding
        centered[idx] = "*" + " " * left_padding + unpadded_line + " " * right_padding + "*"
    return centered


def main():
    picture = [
        "*************",
        "* hello     *",
        "* my name   *",
        "* is Altug! *",
        "*************",
    ]
    centered = center(picture)

    size = len(picture)
    for i in range(size):
        arrow = "=>" if i == size // 2 else "  "
        print(f"{picture[i]}    {arrow}    {centered[i]}")


if __name__ == "__main__":
    main()
