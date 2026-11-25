from token_stream import TokenStream
from vec import Vec


def read_all_vec(cls):
    """Read records of `cls` into a Vec; return (students, maxlen)."""
    stream = TokenStream()
    students = Vec()
    while True:
        record = cls()
        if not record.read(stream):
            break
        students.push_back(record)
    maxlen = max((len(s.name()) for s in students), default=0)
    return students, maxlen
