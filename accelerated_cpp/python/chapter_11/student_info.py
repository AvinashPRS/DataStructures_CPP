# Exercise 11-5: Student_info that reports every create/copy/assign/destroy.
import copy

from grade import grade as _grade


class StudentInfo:
    def __init__(self, stream=None):
        print("create")
        self._n = ""
        self.midterm = 0.0
        self.final = 0.0
        self.homework = []
        if stream is not None:
            self.read(stream)

    def __copy__(self):
        print("copy")
        new = object.__new__(StudentInfo)
        new._n = self._n
        new.midterm = self.midterm
        new.final = self.final
        new.homework = list(self.homework)
        return new

    def assign(self, rhs):
        print("assign")
        self._n = rhs._n
        self.midterm = rhs.midterm
        self.final = rhs.final
        self.homework = list(rhs.homework)
        return self

    def __del__(self):
        print("destroy")

    def name(self):
        return self._n

    def valid(self):
        return len(self.homework) != 0

    def read(self, stream):
        self._n = stream.word()
        self.midterm = stream.number()
        self.final = stream.number()
        if stream:
            self.homework = stream.numbers()
        return stream

    def grade(self):
        return _grade(self.midterm, self.final, self.homework)


def compare(s):
    return s.name()


def read_students(stream):
    """Read every record, copying it into the result like push_back does."""
    students = []
    record = StudentInfo()
    while record.read(stream):
        students.append(copy.copy(record))
    return students
