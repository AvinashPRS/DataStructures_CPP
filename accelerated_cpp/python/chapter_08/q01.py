# Chapter 8, exercise 1: generic analysis taking any grading function.
import sys

from _paths import use_chapter

use_chapter(6)
from _partition import read_partitioned  # noqa: E402
from analysis import average_grade, grade_aux, optimistic_median  # noqa: E402
from median import median  # noqa: E402


def analysis_tmp(students, grade_function):
    return median([grade_function(s) for s in students])


def write_analysis_tmp(out, name, grade_function, did, didnt):
    out.write(f"{name}: median(did) = {analysis_tmp(did, grade_function):g}, "
              f"median(didnt) = {analysis_tmp(didnt, grade_function):g}\n")


def main():
    parts = read_partitioned()
    if parts is None:
        return 1
    did, didnt = parts
    write_analysis_tmp(sys.stdout, "median", grade_aux, did, didnt)
    write_analysis_tmp(sys.stdout, "average", average_grade, did, didnt)
    write_analysis_tmp(sys.stdout, "median of homework turned in", optimistic_median, did, didnt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
