# Exercise 15-6: the Picture classes built on chapter 12's Vec and Str.
from _paths import use_chapter
from pic import frame, hcat, vcat  # noqa: F401
from pic import Picture as _Picture

use_chapter(12)
from str_class import Str  # noqa: E402,F401
from vec import Vec  # noqa: E402,F401


class Picture(_Picture):
    def __init__(self, rows=None, _p=None):
        # rows is a Vec<Str>; each Str is rendered via str()
        super().__init__(list(rows) if rows is not None else [], _p)
