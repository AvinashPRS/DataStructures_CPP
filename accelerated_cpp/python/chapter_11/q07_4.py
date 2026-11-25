# Chapter 11, exercise 7 (redo 9-4 with Vec): check valid() first.
from student_info_vec import StudentInfo


def main():
    student = StudentInfo()
    if student.valid():
        student.grade()


if __name__ == "__main__":
    main()
