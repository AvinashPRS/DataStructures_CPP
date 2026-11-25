# Chapter 11, exercise 5 (part 1): count Student_info lifecycle events while
# running the chapter 6 analyses.
import copy
import sys

from _ch06 import analysis
from student_info import StudentInfo
from token_stream import TokenStream


def read_partitioned():
    did, didnt = [], []
    stream = TokenStream()
    student = StudentInfo()
    while student.read(stream):
        (did if analysis.did_all_hw(student) else didnt).append(copy.copy(student))
    if not did:
        print("No student did all the homework!")
        return None
    if not didnt:
        print("Every student did all the homework!")
        return None
    return did, didnt


def main():
    parts = read_partitioned()
    if parts is None:
        return 1
    did, didnt = parts
    analysis.write_analysis(sys.stdout, "median", analysis.median_analysis, did, didnt)
    analysis.write_analysis(sys.stdout, "average", analysis.average_analysis, did, didnt)
    analysis.write_analysis(sys.stdout, "median of homework turned in",
                            analysis.optimistic_median_analysis, did, didnt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
