# Helper to import modules written for earlier chapters.
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def use_chapter(n):
    path = os.path.join(_HERE, "..", f"chapter_{n:02d}")
    if path not in sys.path:
        sys.path.append(path)  # after this chapter, so local modules win
