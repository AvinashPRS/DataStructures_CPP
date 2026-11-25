# Chapter 4, exercise 4: same as exercise 3 but with doubles.


def get_length(number, decimal_points):
    length = 1
    while number / 10 > 1.0:
        number /= 10
        length += 1
    return length + decimal_points + 1


def main():
    max_number = 1000.0
    decimal_points = 2
    max_len = get_length(max_number, decimal_points)
    max_sq = get_length(max_number * max_number, decimal_points)

    i = 1.0
    while i < max_number:
        print(f"{i:{max_len}.{decimal_points}f}{i * i:{max_sq + 1}.{decimal_points}f}")
        i += 1


if __name__ == "__main__":
    main()
