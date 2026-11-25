"""Traveling Salesman Problem: nearest neighbor + 2-opt. Usage: python3 main.py [input_file]"""
import sys

from algorithms import Tsp


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} input_file")
        return 1

    test = Tsp(sys.argv[1])  # read in command line input
    test.nearest_neighbor()  # run nearest neighbor function
    return 0


if __name__ == "__main__":
    sys.exit(main())
