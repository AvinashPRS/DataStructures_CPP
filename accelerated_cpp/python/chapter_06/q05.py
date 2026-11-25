# Chapter 6, exercise 5: analysis using optimistic_median (§6.2.2/114).
import sys

from _partition import read_partitioned
from analysis import (average_analysis, median_analysis,
                      optimistic_median_analysis, write_analysis)


def main():
    parts = read_partitioned()
    if parts is None:
        return 1
    did, didnt = parts
    write_analysis(sys.stdout, "median", median_analysis, did, didnt)
    write_analysis(sys.stdout, "average", average_analysis, did, didnt)
    write_analysis(sys.stdout, "median of homework turned in",
                   optimistic_median_analysis, did, didnt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
