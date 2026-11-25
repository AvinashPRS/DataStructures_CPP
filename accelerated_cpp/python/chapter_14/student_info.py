# Core/Grad hierarchy and a Student_info handle that uses Ptr (exercise 14-3).
import copy

from _paths import use_chapter
from ptr import Ptr

use_chapter(4)
from grade import grade as _grade  # noqa: E402


class Core:
    def __init__(self, stream=None):
        self._n = ""
        self.midterm = 0.0
        self.final = 0.0
        self.homework = []
        if stream is not None:
            self.read(stream)

    def name(self):
        return self._n

    def grade(self):
        return _grade(self.midterm, self.final, self.homework)

    def read_common(self, stream):
        self._n = stream.word()
        self.midterm = stream.number()
        self.final = stream.number()
        return stream

    def read(self, stream):
        self.read_common(stream)
        if stream:
            self.homework = stream.numbers()
        return stream

    def clone(self):
        return copy.deepcopy(self)


class Grad(Core):
    def __init__(self, stream=None):
        self.thesis = 0.0
        super().__init__(stream)

    def read(self, stream):
        self.read_common(stream)
        self.thesis = stream.number()
        if stream:
            self.homework = stream.numbers()
        return stream

    def grade(self):
        return min(super().grade(), self.thesis)


class StudentInfo:
    def __init__(self, stream=None):
        self._cp = Ptr()
        if stream is not None:
            self.read(stream)

    def __copy__(self):
        new = StudentInfo()
        new._cp = self._cp.copy()
        return new

    def read(self, stream):
        ch = stream.char()
        if not stream:
            return stream
        self._cp = Ptr(Core(stream) if ch == "U" else Grad(stream))
        return stream

    def name(self):
        if not self._cp:
            raise RuntimeError("uninitialized Student")
        return self._cp.get().name()

    def grade(self):
        if not self._cp:
            raise RuntimeError("uninitialized Student")
        return self._cp.get().grade()

    @staticmethod
    def compare(s):
        return s.name()


def compare_core_ptrs(p):
    """Sort key for a list of Ptr<Core>."""
    return p.get().name()


def read_core_ptrs(stream):
    """Read records into a list of Ptr<Core> (§14.1.2)."""
    students = []
    record = Ptr()
    while True:
        ch = stream.char()
        if not stream:
            break
        record.assign(Ptr(Core() if ch == "U" else Grad()))
        record.get().read(stream)  # virtual call
        students.append(record.copy())
    return students
