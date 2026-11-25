# Chapter 10, exercise 3: median works on arrays and vectors alike and does
# not modify its argument.
import array

from q02 import median


def fmt(seq):
    return ", ".join(f"{x:g}" for x in seq)


def main():
    double_arr = array.array("d", [7.5, 2.2, 1.5, 6.4, 4.9, 5.8, 9.4])
    double_vec = list(double_arr)

    print("Initial values of the array: " + fmt(double_arr))
    print("Initial values of the vector: " + fmt(double_vec))
    print(f"The median value for the array: {median(double_arr):g}")
    print(f"The median value for the vector: {median(double_vec):g}")
    print("Final values of the array: " + fmt(double_arr))
    print("Final values of the vector: " + fmt(double_vec))


if __name__ == "__main__":
    main()
