# Chapter 14, exercise 1: store Ptr<Core> objects and sort them.
# Usage: python q01.py < student_list.txt   (U/G records only)
from student_info import compare_core_ptrs, read_core_ptrs
from token_stream import TokenStream


def main():
    students = read_core_ptrs(TokenStream())
    students.sort(key=compare_core_ptrs)
    for p in students:
        print(p.get().name())


if __name__ == "__main__":
    main()
