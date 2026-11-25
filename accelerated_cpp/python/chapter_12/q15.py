# Chapter 12, exercise 15: after end-of-file the stream stays in a failed
# state, so the second loop never runs.
from str_class import CharStream, Str, read_word


def main():
    stream = CharStream()
    s = Str()
    while read_word(stream, s):
        print(f"1: {s}")
    # the stream is still at end-of-file, so this loop is skipped
    while read_word(stream, s):
        print(f"2: {s}")


if __name__ == "__main__":
    main()
