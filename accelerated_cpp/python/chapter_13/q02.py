# Chapter 13, exercise 2: trace which grade()/name() is called.
import student_info
from student_info import Core, Grad


def main():
    p1 = Core()
    p2 = Grad()
    s1 = Core()
    s2 = Grad()
    student_info.TRACE = True

    for obj in (p1, p2, s1, s2):
        try:
            obj.grade()
        except ValueError:
            pass
        obj.name()


if __name__ == "__main__":
    main()
