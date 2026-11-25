# Shared helper for the chapter 2 framing exercises.


def write_frame(greeting, pad_vertical, pad_horizontal):
    """Write `greeting` inside a frame of asterisks, mirroring the
    character-by-character loop from the book."""
    rows = pad_vertical * 2 + 3
    cols = len(greeting) + pad_horizontal * 2 + 2

    print()
    # invariant: we have written r rows so far
    for r in range(rows):
        c = 0
        line = []
        # invariant: we have written c characters so far in the current row
        while c != cols:
            # is it time to write the greeting?
            if r == pad_vertical + 1 and c == pad_horizontal + 1:
                line.append(greeting)
                c += len(greeting)
            else:
                # are we on the border?
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    line.append("*")
                else:
                    line.append(" ")
                c += 1
        print("".join(line))


def read_first_name():
    return input("Please enter your first name: ").split()[0]
