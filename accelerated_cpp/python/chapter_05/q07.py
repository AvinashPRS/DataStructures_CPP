# Chapter 5, exercise 7: what does frame do with an empty picture?
from frame import frame


def main():
    for line in frame([]):
        print(line)


if __name__ == "__main__":
    main()
