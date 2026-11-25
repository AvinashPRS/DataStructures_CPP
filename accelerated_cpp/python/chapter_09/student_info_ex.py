# Exercise 9-1: compute and store the grade while reading.
from _paths import use_chapter
from token_stream import TokenStream

use_chapter(4)
from grade import grade as _grade  # noqa: E402


class StudentInfo:
    def __init__(self, stream=None):
        self._n = ""
        self._g = 0.0
        self._error = None
        self.midterm = 0.0
        self.final = 0.0
        self.homework = []
        if stream is not None:
            self.read(stream)

    def name(self):
        return self._n

    def valid(self):
        return len(self.homework) != 0

    def read(self, stream: TokenStream):
        self._n = stream.word()
        self.midterm = stream.number()
        self.final = stream.number()
        if stream:
            self.homework = stream.numbers()
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
