# Chapter 11, exercise 5 (part 2): same, using per-student metrics.
import sys

from _ch06 import analysis
from q05_1 import read_partitioned


def main():
    parts = read_partitioned()
    if parts is None:
        return 1
    did, didnt = parts
    analysis.write_analysis(sys.stdout, "median", analysis.grade_aux, did, didnt, per_student=True)
    analysis.write_analysis(sys.stdout, "average", analysis.average_grade, did, didnt, per_student=True)
    analysis.write_analysis(sys.stdout, "median of homework turned in",
                            analysis.optimistic_median, did, didnt, per_student=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
