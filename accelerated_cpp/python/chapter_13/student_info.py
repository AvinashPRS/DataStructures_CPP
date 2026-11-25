# Inheritance-based student records (chapter 13).
import copy

from _paths import use_chapter

use_chapter(4)
from grade import grade as _grade  # noqa: E402

NUMBERS = (97, 94, 90, 87, 84, 80, 77, 74, 70, 60, 0)
LETTERS = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F")

# Set to True to trace constructor and grade/name calls (exercises 13-1, 13-2).
TRACE = False


def _trace(msg):
    if TRACE:
        print(msg)


class Core:
    def __init__(self, stream=None):
        self._n = ""
        self.midterm = 0.0
        self.final = 0.0
        self.homework = []
        if stream is not None:
            self.read(stream)
            _trace("Core::Core(istream&)")
        else:
            _trace("Core::Core()")

    def name(self):
        _trace("Core::name()")
        return self._n

    def grade(self):
        _trace("Core::grade()")
        return _grade(self.midterm, self.final, self.homework)

    def read_common(self, stream):
        """§13.1.2/230"""
        self._n = stream.word()
        self.midterm = stream.number()
        self.final = stream.number()
        return stream

    def read(self, stream):
        self.read_common(stream)
        if stream:
            self.homework = stream.numbers()
        return stream

    def valid(self):  # exercise 13-3
        return len(self.homework) != 0

    def letter_grade(self):  # exercise 13-4
        g = self.grade()
        for number, letter in zip(NUMBERS, LETTERS):
            if g >= number:
                return letter
        return "???"

    def meets_requirements(self):  # exercise 13-5
        return self.valid()

    def clone(self):
        return copy.deepcopy(self)


class Grad(Core):
    def __init__(self, stream=None):
        self.thesis = 0.0
        super().__init__(stream)
        _trace("Grad::Grad(istream&)" if stream is not None else "Grad::Grad()")

    def read(self, stream):
        """§13.1.2/230"""
        self.read_common(stream)
        self.thesis = stream.number()
        if stream:
            self.homework = stream.numbers()
        return stream

    def grade(self):
        _trace("Grad::grade()")
        return min(super().grade(), self.thesis)

    def meets_requirements(self):
        return self.thesis != 0


class PassFail(Core):
    """Exercise 13-6: homework is optional."""

    def grade(self):
        if not self.homework:
            return (self.final + self.midterm) / 2
        return super().grade()

    def valid(self):
        return self.midterm > 0 or self.final > 0

    def letter_grade(self):
        return "P" if self.grade() > 60 else "F"


class Audit(PassFail):
    """Exercise 13-7: audited students get no grade."""

    def valid(self):
        return len(self.name()) > 0

    def letter_grade(self):
        return "N/A"


class StudentInfo:
    """Handle class that owns a Core (or derived) object (§13.4)."""

    def __init__(self, stream=None):
        self._cp = None
        if stream is not None:
            self.read(stream)

    def read(self, stream):
        ch = stream.char()  # record type
        if not stream:
            return stream
        if ch == "U":
            self._cp = Core(stream)
        elif ch == "G":
            self._cp = Grad(stream)
        elif ch == "P":
            self._cp = PassFail(stream)
        else:
            self._cp = Audit(stream)
        return stream

    def __copy__(self):
        """§13.4.2/247: copying clones the underlying object."""
        new = StudentInfo()
        if self._cp is not None:
            new._cp = self._cp.clone()
        return new

    def _require(self):
        if self._cp is None:
            raise RuntimeError("uninitialized Student")
        return self._cp

    def name(self):
        return self._require().name()

    def grade(self):
        return self._require().grade()

    def valid(self):
        return self._require().valid()

    def letter_grade(self):
        return self._require().letter_grade()

    def meets_requirements(self):
        return self._require().meets_requirements()

    @staticmethod
    def compare(s):
        """§13.4/244: sort key by name."""
        return s.name()


def compare(c):
    """§13.2/232"""
    return c.name()


def compare_grades(c):
    """§13.2.1/234"""
    return c.grade()


def read_all(stream):
    students = []
    record = StudentInfo()
    while record.read(stream):
        students.append(copy.copy(record))
    maxlen = max((len(s.name()) for s in students), default=0)
    return students, maxlen
