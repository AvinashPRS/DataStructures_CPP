"""Debug / logging helpers (Python version of dbg.h, Zed Shaw's debug macros).

The C macros use `goto error`; in Python `check`/`sentinel` raise CheckError
instead, which the caller catches to run its cleanup code.
Set the environment variable NDEBUG to disable debug().
"""
import inspect
import os
import sys

NDEBUG = bool(os.environ.get("NDEBUG"))

# Python has no global errno; we keep one that callers may set.
errno = 0


class CheckError(Exception):
    """Raised by check()/sentinel() in place of `goto error`."""


def _where():
    frame = inspect.stack()[2]
    return os.path.basename(frame.filename), frame.lineno


def clean_errno():
    return "None" if errno == 0 else os.strerror(errno)


def debug(msg, *args):
    if NDEBUG:
        return
    f, line = _where()
    print(f"DEBUG {f}:{line}: " + (msg % args if args else msg), file=sys.stderr)


def log_err(msg, *args):
    f, line = _where()
    print(f"[ERROR] ({f}:{line}: errno: {clean_errno()}) " +
          (msg % args if args else msg), file=sys.stderr)


def log_warn(msg, *args):
    f, line = _where()
    print(f"[WARN] ({f}:{line}: errno: {clean_errno()}) " +
          (msg % args if args else msg), file=sys.stderr)


def log_info(msg, *args):
    f, line = _where()
    print(f"[INFO] ({f}:{line}) " + (msg % args if args else msg), file=sys.stderr)


def check(cond, msg, *args):
    global errno
    if not cond:
        f, line = _where()
        print(f"[ERROR] ({f}:{line}: errno: {clean_errno()}) " +
              (msg % args if args else msg), file=sys.stderr)
        errno = 0
        raise CheckError(msg % args if args else msg)


def sentinel(msg, *args):
    global errno
    f, line = _where()
    print(f"[ERROR] ({f}:{line}: errno: {clean_errno()}) " +
          (msg % args if args else msg), file=sys.stderr)
    errno = 0
    raise CheckError(msg % args if args else msg)


def check_mem(obj):
    global errno
    if obj is None:
        f, line = _where()
        print(f"[ERROR] ({f}:{line}: errno: {clean_errno()}) Out of memory.",
              file=sys.stderr)
        errno = 0
        raise CheckError("Out of memory.")


def check_debug(cond, msg, *args):
    global errno
    if not cond:
        if not NDEBUG:
            f, line = _where()
            print(f"DEBUG {f}:{line}: " + (msg % args if args else msg),
                  file=sys.stderr)
        errno = 0
        raise CheckError(msg % args if args else msg)


def set_errno(value):
    global errno
    errno = value

