# Chapter 4, exercise 3: column widths adapt to the largest number.


def get_length(number):
    """Number of digits in a non-negative integer."""
    length = 1
    while number // 10 > 0:
        number //= 10
        length += 1
    return length


def main():
    max_number = 999
    max_len = get_length(max_number)
    max_sq = get_length(max_number * max_number)
    for i in range(1, max_number + 1):
        print(f"{i:{max_len}}{i * i:{max_sq + 1}}")


if __name__ == "__main__":
    main()
