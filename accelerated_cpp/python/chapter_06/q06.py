# Chapter 6, exercise 6: one generic analysis function, passed a metric.
import sys

from _partition import read_partitioned
from analysis import average_grade, grade_aux, optimistic_median, write_analysis


def main():
    parts = read_partitioned()
    if parts is None:
        return 1
    did, didnt = parts
    write_analysis(sys.stdout, "median", grade_aux, did, didnt, per_student=True)
    write_analysis(sys.stdout, "average", average_grade, did, didnt, per_student=True)
    write_analysis(sys.stdout, "median of homework turned in",
                   optimistic_median, did, didnt, per_student=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
