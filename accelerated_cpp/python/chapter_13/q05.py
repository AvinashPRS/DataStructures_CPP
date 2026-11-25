# Chapter 13, exercise 5: does each student meet the requirements?
# Usage: python q05.py < student_list.txt
from student_info import read_all
from token_stream import TokenStream


def main():
    students, _ = read_all(TokenStream())
    for s in students:
        status = "meets requirements" if s.meets_requirements() else "does not meet requirements"
        print(f"{s.name()}:\t{status}")


if __name__ == "__main__":
    main()
