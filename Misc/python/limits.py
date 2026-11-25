"""Find the minimum, starting from the largest representable float."""
import sys


def main():
    nums = [5.6, 8.1, 2.3, 10.4, -1.2, 7.8]
    minimum = sys.float_info.max  # std::numeric_limits<double>::max()
    for x in nums:
        if x < minimum:
            minimum = x
    print(f"Minimum = {minimum:g}")


if __name__ == "__main__":
    main()
