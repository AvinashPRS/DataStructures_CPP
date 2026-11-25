"""
Timing copy-construction vs back_inserter-style appending (port of vector_prop.cpp).
"""
import time


# main code harness:
def main():
    u = [100] * 1000000

    # calculate the time for copying
    begin_copy = time.process_time()
    v = list(u)
    end_copy = time.process_time()

    # clear list for the next test
    v.clear()

    # calculate the time for back inserter (append one by one)
    begin_back = time.process_time()
    for x in u:
        v.append(x)
    end_back = time.process_time()

    # write the results
    print(f"copying took {end_copy - begin_copy:g} seconds for {len(u)} items.")
    print(f"back_inserter took {end_back - begin_back:g} seconds for {len(u)} items.")


if __name__ == "__main__":
    main()
