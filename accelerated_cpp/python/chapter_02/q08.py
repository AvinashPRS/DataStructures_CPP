# Chapter 2, exercise 8: product of the numbers in the range [1, 10).


def main():
    product = 1
    for i in range(1, 10):
        product *= i
    print(product)


if __name__ == "__main__":
    main()
