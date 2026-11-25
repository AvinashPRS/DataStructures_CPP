# Chapter 14, exercise 2: names and grades via Ptr<Core>.
from student_info import compare_core_ptrs, read_core_ptrs
from token_stream import TokenStream


def main():
    students = read_core_ptrs(TokenStream())
    maxlen = max((len(p.get().name()) for p in students), default=0)
    students.sort(key=compare_core_ptrs)
    for p in students:
        name = p.get().name()
        print(name + " " * (maxlen + 1 - len(name)), end="")
        try:
            print(f"{p.get().grade():.3g}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
