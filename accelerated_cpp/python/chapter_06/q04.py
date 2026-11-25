# Chapter 6, exercise 4: compare copying a list with appending element-wise.
import time


def main():
    u = [100] * 1000000

    begin_copy = time.process_time()
    v = list(u)
    end_copy = time.process_time()

    v.clear()

    begin_back = time.process_time()
    for x in u:
        v.append(x)
    end_back = time.process_time()

    print(f"copying took {end_copy - begin_copy:g} seconds for {len(u)} items.")
    print(f"back_inserter took {end_back - begin_back:g} seconds for {len(u)} items.")


if __name__ == "__main__":
    main()
