# Chapter 4, exercise 2: squares of the integers 1..100 in two columns.


def main():
    for i in range(1, 101):
        print(f"{i:3}{i * i:6}")


if __name__ == "__main__":
    main()
