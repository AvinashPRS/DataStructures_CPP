# Character pictures built from shared sub-pictures (chapter 15).
# Python references play the role of Ptr<Pic_base>: sub-pictures are shared,
# never copied.
import sys
from abc import ABC, abstractmethod


class PicBase(ABC):
    @abstractmethod
    def width(self): ...

    @abstractmethod
    def height(self): ...

    @abstractmethod
    def display(self, os, row, do_pad): ...

    @abstractmethod
    def reframe(self, tb, lr, c): ...  # exercise 15-4

    @staticmethod
    def pad(os, beg, end):
        if end > beg:
            os.write(" " * (end - beg))


class StringPic(PicBase):
    def __init__(self, rows):
        self.data = [str(r) for r in rows]

    def height(self):
        return len(self.data)

    def width(self):
        """§15.2.2/281"""
        return max((len(r) for r in self.data), default=0)

    def display(self, os, row, do_pad):
        """§15.2.2/282"""
        start = 0
        if row < self.height():
            os.write(self.data[row])
            start = len(self.data[row])
        if do_pad:
            self.pad(os, start, self.width())

    def reframe(self, tb, lr, c):
        pass


class FramePic(PicBase):
    """Exercises 15-2/15-3: configurable border characters."""

    def __init__(self, p, tb="*", lr="*", c="*"):
        self.p, self.tb, self.lr, self.c = p, tb, lr, c

    def width(self):
        return self.p.width() + 4

    def height(self):
        return self.p.height() + 4

    def display(self, os, row, do_pad):
        if row >= self.height():
            if do_pad:
                self.pad(os, 0, self.width())
        elif row == 0 or row == self.height() - 1:
            os.write(self.c + self.tb * (self.width() - 2) + self.c)
        elif row == 1 or row == self.height() - 2:
            os.write(self.lr)
            self.pad(os, 1, self.width() - 1)
            os.write(self.lr)
        else:
            os.write(self.lr + " ")
            self.p.display(os, row - 2, True)
            os.write(" " + self.lr)

    def reframe(self, tb, lr, c):
        self.tb, self.lr, self.c = tb, lr, c
        self.p.reframe(tb, lr, c)


class VCatPic(PicBase):
    def __init__(self, top, bottom):
        self.top, self.bottom = top, bottom

    def width(self):
        return max(self.top.width(), self.bottom.width())

    def height(self):
        return self.top.height() + self.bottom.height()

    def display(self, os, row, do_pad):
        """§15.2.4/284"""
        w = 0
        if row < self.top.height():
            self.top.display(os, row, do_pad)
            w = self.top.width()
        elif row < self.height():
            self.bottom.display(os, row - self.top.height(), do_pad)
            w = self.bottom.width()
        if do_pad:
            self.pad(os, w, self.width())

    def reframe(self, tb, lr, c):
        self.top.reframe(tb, lr, c)
        self.bottom.reframe(tb, lr, c)


class HCatPic(PicBase):
    def __init__(self, left, right):
        self.left, self.right = left, right

    def width(self):
        return self.left.width() + self.right.width()

    def height(self):
        return max(self.left.height(), self.right.height())

    def display(self, os, row, do_pad):
        """Exercise 15-5: vertically center the shorter picture."""
        lh, rh = self.left.height(), self.right.height()
        if lh >= rh:
            diff = lh - rh
            self.left.display(os, row, True)
            if row >= diff // 2:
                self.right.display(os, row - diff // 2, do_pad)
            elif do_pad:
                self.pad(os, 0, self.right.width())
        else:
            diff = rh - lh
            if row >= diff // 2:
                self.left.display(os, row - diff // 2, True)
            else:
                self.left.display(os, lh, True)  # out of range: padding only
            self.right.display(os, row, do_pad)

    def reframe(self, tb, lr, c):
        self.left.reframe(tb, lr, c)
        self.right.reframe(tb, lr, c)


class Picture:
    def __init__(self, rows=(), _p=None):
        """§15.2.1/280"""
        self.p = _p if _p is not None else StringPic(rows)

    def reframe(self, tb, lr, c):
        self.p.reframe(tb, lr, c)

    def write(self, os=sys.stdout):
        for i in range(self.p.height()):
            self.p.display(os, i, False)
            os.write("\n")

    def __str__(self):
        import io
        buf = io.StringIO()
        self.write(buf)
        return buf.getvalue()


def _as_picture(x):
    return x if isinstance(x, Picture) else Picture(x)


def frame(pic, tb="*", lr="*", c="*"):
    """§15.2.1/279"""
    return Picture(_p=FramePic(_as_picture(pic).p, tb, lr, c))


def hcat(l, r):
    return Picture(_p=HCatPic(_as_picture(l).p, _as_picture(r).p))


def vcat(t, b):
    return Picture(_p=VCatPic(_as_picture(t).p, _as_picture(b).p))
