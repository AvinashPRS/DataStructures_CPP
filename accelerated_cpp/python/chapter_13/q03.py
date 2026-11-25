# Chapter 13, exercise 3: check valid() before grading.
from student_info import Grad


def main():
    p = Grad()
    if p.valid():
        p.grade()


if __name__ == "__main__":
    main()
