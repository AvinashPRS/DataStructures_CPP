# Chapter 11, exercise 9: doubling capacity vs. growing one slot at a time.
import time

from vec import Vec


def main():
    count = 100000
    v1, v2 = Vec(), Vec()

    begin = time.process_time()
    for i in range(count):
        v1.push_back(i)
    end = time.process_time()
    print(f"Doubling memory and pushing {count} integers took {end - begin:g} seconds.")

    # growing by one copies the whole array every time: O(n^2)
    begin = time.process_time()
    for i in range(count):
        v2.push_back_grow_once(i)
    end = time.process_time()
    print(f"Growing memory one by one and pushing {count} integers took {end - begin:g} seconds.")


if __name__ == "__main__":
    main()
