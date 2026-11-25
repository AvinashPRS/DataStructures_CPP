"""Exercise 8-5: modify fsize to print the other information contained in
the inode entry (printed similarly to ls -l)."""
import grp
import os
import pwd
import stat
import sys
import time

MAX_PATH_LEN = 1024


def print_file_flags(mode):
    flags = "d" if stat.S_ISDIR(mode) else "-"
    for bit, ch in ((stat.S_IRUSR, "r"), (stat.S_IWUSR, "w"),
                    (stat.S_IXUSR, "x"), (stat.S_IRGRP, "r"),
                    (stat.S_IWGRP, "w"), (stat.S_IXGRP, "x"),
                    (stat.S_IROTH, "r"), (stat.S_IWOTH, "w"),
                    (stat.S_IXOTH, "x")):
        flags += ch if mode & bit else "-"
    sys.stdout.write(flags + " ")


def print_file_user(uid):
    try:
        sys.stdout.write(pwd.getpwuid(uid).pw_name + " ")
    except KeyError:
        sys.stderr.write("Error: cannot find user\n")


def print_file_group(gid):
    try:
        sys.stdout.write(grp.getgrgid(gid).gr_name + " ")
    except KeyError:
        sys.stderr.write("Error: cannot find group\n")


def print_file_size(size):
    sizes = ["B", "K", "M", "G"]
    div = 0
    rem = 0
    while size >= 1024 and div < len(sizes) - 1:
        rem = size % 1024
        div += 1
        size //= 1024
    sys.stdout.write("%6.1f%s " % (size + rem / 1024.0, sizes[div]))


def print_file_time(t):
    sys.stdout.write(time.strftime("%d %b %H:%M", time.localtime(t)) + " ")


def dir_walk(dir_name, func):
    try:
        entries = os.listdir(dir_name)
    except OSError:
        sys.stderr.write("dir_walk: cannot open %s\n" % dir_name)
        return

    for entry in entries:  # listdir already skips "." and ".."
        if len(dir_name) + len(entry) + 2 > MAX_PATH_LEN:
            sys.stderr.write("dir_walk: path too long\n")
        else:
            func("%s/%s" % (dir_name, entry))


def fsize(name):
    try:
        st = os.stat(name)
    except OSError:
        sys.stderr.write("fsize: cannot access %s\n" % name)
        return

    if stat.S_ISDIR(st.st_mode):
        dir_walk(name, fsize)

    print_file_flags(st.st_mode)
    sys.stdout.write("%d " % st.st_nlink)
    print_file_user(st.st_uid)
    print_file_group(st.st_gid)
    print_file_size(st.st_size)
    print_file_time(st.st_atime)
    print(name)


def main(argv):
    if len(argv) == 1:
        fsize(".")
    else:
        for name in argv[1:]:
            fsize(name)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
