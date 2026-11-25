# Rotations used to build a permuted index (chapter 5 exercise 1).
from dataclasses import dataclass, field
from functools import cmp_to_key

from split import split


@dataclass
class Rotation:
    words: list = field(default_factory=list)
    start: int = 0


def get_rotations(line):
    """Return every rotation of the words in `line`."""
    rotations = []
    words = split(line)
    size = len(words)
    for i in range(size):
        r = Rotation(start=(size - i) % size)
        r.words = [words[(j + i) % size] for j in range(size)]
        rotations.append(r)
    return rotations


def first_width(rotation):
    """Width of the part of the original line that precedes the
    rotation's first word."""
    width = 0
    if rotation.start != 0:
        size = len(rotation.words)
        for i in range(rotation.start, size):
            width += len(rotation.words[i])
        width += size - rotation.start - 1
    return width


def max_first_width(rotations):
    """Longest first part among all rotations."""
    longest = 0
    for r in rotations:
        if r.start == 1:
            longest = max(longest, first_width(r))
    return longest


def format_rotation(rotation, max_width):
    """Unrotate the rotation and pad it so the index word lines up."""
    width = first_width(rotation)
    words = list(rotation.words)

    if rotation.start == 0:
        words[0] = " " * 5 + words[0]
    else:
        words[0] = " " * 4 + words[0]

    words[rotation.start] = " " * (max_width - width) + words[rotation.start]

    size = len(words)
    return " ".join(words[(rotation.start + i) % size] for i in range(size))


def _compare(x, y):
    """Case-insensitive comparison of the first words; on a tie,
    lowercase sorts before uppercase."""
    word_x = x.words[0].lower()
    word_y = y.words[0].lower()
    if word_x != word_y:
        return -1 if word_x < word_y else 1
    a, b = x.words[0], y.words[0]
    if a == b:
        return 0
    return -1 if a > b else 1


compare = cmp_to_key(_compare)
