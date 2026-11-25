# Student_info whose homework is stored in a Vec.
from grade import grade as _grade
from vec import Vec


class StudentInfo:
    def __init__(self, stream=None):
        self._n = ""
        self.midterm = 0.0
        self.final = 0.0
        self.homework = Vec()
        if stream is not None:
            self.read(stream)

    def name(self):
        return self._n

    def valid(self):
        return not self.homework.empty()

    def read(self, stream):
        self._n = stream.word()
        self.midterm = stream.number()
        self.final = stream.number()
        if stream:
            self.homework = Vec(iterable=stream.numbers())
        return stream

    def grade(self):
        return _grade(self.midterm, self.final, self.homework)


def compare(s):
    return s.name()
