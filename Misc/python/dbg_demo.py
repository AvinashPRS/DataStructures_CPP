"""Exercises the debug macros in dbg.py (Python version of dbg.c).
Usage: python3 dbg_demo.py <some_file_that_does_not_exist>"""
import errno as _errno
import sys

import dbg
from dbg import (CheckError, check, check_debug, check_mem, debug, log_err,
                 log_info, log_warn, sentinel)


def test_debug():
    # notice you don't need the \n
    debug("I have Brown Hair.")
    # passing in arguments like printf
    debug("I am %d years old.", 37)


def test_log_err():
    log_err("I believe everything is broken.")
    log_err("There are %d problems in %s.", 0, "space")


def test_log_warn():
    log_warn("You can safely ignore this.")
    log_warn("Maybe consider looking at: %s.", "/etc/passwd")


def test_log_info():
    log_info("Well I did something mundane.")
    log_info("It happened %f times today.", 1.3)


def test_check(file_name):
    block = None
    inp = None
    try:
        block = bytearray(100)
        check_mem(block)  # should work
        try:
            inp = open(file_name, "r")
        except OSError as e:
            dbg.set_errno(e.errno or _errno.ENOENT)
        check(inp, "Failed to open %s.", file_name)
        inp.close()
        return 0
    except CheckError:
        if inp:
            inp.close()
        return -1


def test_sentinel(code):
    try:
        temp = bytearray(100)
        check_mem(temp)
        if code == 1:
            log_info("It worked.")
        else:
            sentinel("I shouldn't run.")
        return 0
    except CheckError:
        return -1


def test_check_mem():
    try:
        test = None
        check_mem(test)
        return 1
    except CheckError:
        return -1


def test_check_debug():
    try:
        i = 0
        check_debug(i != 0, "Oops, I was 0.")
        return 0
    except CheckError:
        return -1


def main(argv):
    try:
        check(len(argv) == 2, "Need an argument.")

        test_debug()
        test_log_err()
        test_log_warn()
        test_log_info()

        check(test_check(__file__) == 0, "failed with %s", __file__)
        check(test_check(argv[1]) == -1, "failed with argv")
        check(test_sentinel(1) == 0, "test_sentinel failed.")
        check(test_sentinel(100) == -1, "test_sentinel failed.")
        check(test_check_mem() == -1, "test_check_mem failed.")
        check(test_check_debug() == -1, "test_check_debug failed.")
        return 0
    except CheckError:
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
