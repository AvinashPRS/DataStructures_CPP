"""Exercise 8-3: design and write _flushbuf, fflush and fclose.

Copies syscalls.py into out.txt using the buffered getc/putc.
The C version also contains syscalls.h; both are merged into this file.
"""
import os
import sys

EOF = -1
BUFFER_SIZE = 1024
MAX_NR_OF_OPEN_FILES = 20
PERMISSIONS = 0o666  # RW for owner, group, others

SEEK_SET = 0  # Set file offset to offset
SEEK_CUR = 1  # Set file offset to current plus offset
SEEK_END = 2  # Set file offset to EOF plus offset


class Flags:
    """Equivalent of the C bit-field struct."""

    def __init__(self, read=False, write=False, unbuf=False):
        self.READ = read
        self.WRITE = write
        self.UNBUF = unbuf
        self.EOF = False
        self.ERR = False


class File:
    """Equivalent of struct _io_buffer_file (FILE)."""

    def __init__(self, fd=-1, flags=None):
        self.counter = 0
        self.pos = 0          # next_char_pos_p as an index into base
        self.base = None      # bytearray buffer
        self.flag = flags or Flags()
        self.file_descriptor = fd


_io_buffer = [File(0, Flags(read=True)),                 # stdin
              File(1, Flags(write=True)),                # stdout
              File(2, Flags(write=True, unbuf=True))]    # stderr
_io_buffer += [File() for _ in range(MAX_NR_OF_OPEN_FILES - 3)]

stdin, stdout, stderr = _io_buffer[0], _io_buffer[1], _io_buffer[2]


def _buffer_size(fp):
    return 1 if fp.flag.UNBUF else BUFFER_SIZE


def _fill_buffer(fp):
    if not fp.flag.READ or fp.flag.EOF or fp.flag.ERR:
        return EOF

    size = _buffer_size(fp)
    try:
        data = os.read(fp.file_descriptor, size)
    except OSError:
        fp.flag.ERR = True
        fp.counter = 0
        return EOF

    if not data:
        fp.flag.EOF = True
        fp.counter = 0
        return EOF

    fp.base = bytearray(data)
    fp.pos = 0
    fp.counter = len(data) - 1
    c = fp.base[fp.pos]
    fp.pos += 1
    return c


def getc(fp):
    """Macro getc from syscalls.h."""
    fp.counter -= 1
    if fp.counter >= 0:
        c = fp.base[fp.pos]
        fp.pos += 1
        return c
    return _fill_buffer(fp)


def file_open(name, mode):
    if mode[:1] not in ("r", "w", "a"):
        return None

    fp = next((f for f in _io_buffer
               if not f.flag.READ and not f.flag.WRITE), None)
    if fp is None:
        return None  # no free slots

    try:
        if mode[0] == "w":
            fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
                         PERMISSIONS)
        elif mode[0] == "a":
            fd = os.open(name, os.O_WRONLY | os.O_CREAT, PERMISSIONS)
            os.lseek(fd, 0, SEEK_END)
        else:
            fd = os.open(name, os.O_RDONLY)
    except OSError:
        return None  # couldn't access name

    fp.file_descriptor = fd
    fp.counter = 0
    fp.pos = 0
    fp.base = None
    fp.flag = Flags(read=(mode[0] == "r"), write=(mode[0] != "r"))
    return fp


def _flush_buffer(c, fp):
    if not fp.flag.WRITE or fp.flag.ERR:
        return EOF

    size = _buffer_size(fp)
    if fp.base is None:
        fp.base = bytearray(size)
    elif fp.pos:
        data = bytes(fp.base[:fp.pos])
        if os.write(fp.file_descriptor, data) != len(data):
            fp.flag.ERR = True
            return EOF

    fp.pos = 0
    if c is not None:
        fp.base[fp.pos] = c
        fp.pos += 1
        fp.counter = size - 1
    else:
        fp.counter = size
    return c


def putc(c, fp):
    """Macro putc from syscalls.h."""
    fp.counter -= 1
    if fp.counter >= 0:
        fp.base[fp.pos] = c
        fp.pos += 1
        return c
    return _flush_buffer(c, fp)


def file_flush(fp):
    if not fp.flag.WRITE:
        fp.flag.ERR = True
        return EOF
    if fp.base is not None and _flush_buffer(None, fp) == EOF:
        return EOF
    return 0


def file_close(fp):
    if fp.flag.WRITE and file_flush(fp) == EOF:
        return EOF

    fp.base = None
    fp.pos = 0
    fp.counter = 0
    os.close(fp.file_descriptor)
    fp.flag = Flags()
    return 0


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    file_in = file_open(os.path.join(here, "syscalls.py"), "r")
    if file_in is None:
        os.write(1, b"Error: could not open the file.\n")
        return 1

    file_out = file_open(os.path.join(here, "out.txt"), "w")
    if file_out is None:
        os.write(1, b"Error: could not open the file.\n")
        return 1

    while True:
        c = getc(file_in)
        if c == EOF:
            break
        putc(c, file_out)

    file_close(file_in)
    file_close(file_out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
