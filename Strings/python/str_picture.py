"""Center the text lines inside a framed ("*" bordered) picture."""


def center(picture):
    centered_picture = list(picture)
    # the picture is assumed to be rectangular
    width = len(centered_picture[0]) - 2

    # skip first and last lines
    for idx in range(1, len(centered_picture) - 1):
        # remove the border "*" characters and collapse the words
        unpadded_line = " ".join(centered_picture[idx][1:width + 1].split())
        # get the size of the paddings
        left_padding = (width - len(unpadded_line)) // 2
        right_padding = width - len(unpadded_line) - left_padding
        # set centered line
        centered_picture[idx] = "*" + " " * left_padding + unpadded_line + " " * right_padding + "*"

    return centered_picture


if __name__ == "__main__":
    # create a picture
    picture = [
        "*************",
        "* hello     *",
        "* my name   *",
        "* is Altug! *",
        "*************",
    ]

    centered_picture = center(picture)

    # picture and centered_picture have the same size
    size = len(picture)
    for i in range(size):
        arrow = "=>" if i == size // 2 else "  "
        print(f"{picture[i]}    {arrow}    {centered_picture[i]}")
