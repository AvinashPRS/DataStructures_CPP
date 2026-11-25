# Exercise 9-5: pass/fail student record with only midterm and final.
from token_stream import TokenStream


class StudentInfo:
    def __init__(self, stream=None):
        self._n = ""
        self.midterm = 0.0
        self.final = 0.0
        if stream is not None:
            self.read(stream)

    def name(self):
        return self._n

    def read(self, stream: TokenStream):
        self._n = stream.word()
        self.midterm = stream.number()
        self.final = stream.number()
        return stream

    def grade(self):
        return "P" if (self.midterm + self.final) / 2 > 60 else "F"


def compare(s):
    return s.name()
