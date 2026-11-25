# Chapter 11, exercise 7 (redo 9-3 part 2 with Vec): catch the error.
from student_info_vec import StudentInfo


def main():
    try:
        StudentInfo().grade()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
