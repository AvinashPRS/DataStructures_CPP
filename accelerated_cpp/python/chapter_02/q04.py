# Chapter 2, exercise 4: write the blanks in chunks instead of one at a time.
from framing import read_first_name


def main():
    name = read_first_name()
    greeting = "Hello, " + name + "!"
    pad = 1

    rows = pad * 2 + 3
    cols = len(greeting) + pad * 2 + 2

    print()
    for r in range(rows):
        c = 0
        line = []
        while c != cols:
            if r == pad + 1 and c == pad + 1:
                line.append(greeting)
                c += len(greeting)
            else:
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    line.append("*")
                    c += 1
                elif r == pad + 1:
                    line.append(" " * pad)
                    c += pad
                else:
                    line.append(" " * (cols - 2))
                    c += cols - 2
        print("".join(line))


if __name__ == "__main__":
    main()
