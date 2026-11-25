import sys


def read_words(stream=sys.stdin):
    """Read every whitespace-separated word from the stream."""
    return stream.read().split()
