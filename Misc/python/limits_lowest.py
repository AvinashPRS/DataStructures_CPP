"""Find the maximum, starting from the lowest representable float."""
import sys


def main():
    nums = [5.6, 8.1, 2.3, 10.4, -1.2]
    maximum = -sys.float_info.max  # std::numeric_limits<double>::lowest()
    for x in nums:
        if x > maximum:
            maximum = x
    print(f"{maximum:g}")


if __name__ == "__main__":
    main()
