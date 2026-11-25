# Student_info (grade computed on read) using Vec for homework.
from grade import grade as _grade
from vec import Vec


class StudentInfo:
    def __init__(self, stream=None):
        self._n = ""
        self._g = 0.0
        self._error = None
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
            try:
                self._g = _grade(self.midterm, self.final, self.homework)
                self._error = None
            except ValueError as e:
                self._error = e
        return stream

    def grade(self):
        if self._error is not None:
            raise self._error
        return self._g


def compare(s):
    return s.name()
