from token_stream import TokenStream


def read_all(cls):
    """Read records of `cls` until input runs out; return (records, maxlen)."""
    stream = TokenStream()
    students = []
    while True:
        record = cls()
        if not record.read(stream):
            break
        students.append(record)
    maxlen = max((len(s.name()) for s in students), default=0)
    return students, maxlen
