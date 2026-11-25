# Student_info as a class (§9.2-9.3).
from _paths import use_chapter
from token_stream import TokenStream

use_chapter(4)
from grade import grade as _grade  # noqa: E402


class StudentInfo:
    def __init__(self, stream=None):
        self._n = ""
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
        """§9.2.1/157"""
        self._n = stream.word()
        self.midterm = stream.number()
        self.final = stream.number()
        if stream:
            self.homework = stream.numbers()
        return stream

    def grade(self):
        """§9.3.1/158"""
        return _grade(self.midterm, self.final, self.homework)


def compare(s):
    """Sort key: by name (§9.3.1/162)."""
    return s.name()
