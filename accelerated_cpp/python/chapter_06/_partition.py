# Read students and split them by whether they did all their homework.
from analysis import did_all_hw
from student_info import read_students


def read_partitioned():
    did, didnt = [], []
    for s in read_students():
        (did if did_all_hw(s) else didnt).append(s)
    if not did:
        print("No student did all the homework!")
        return None
    if not didnt:
        print("Every student did all the homework!")
        return None
    return did, didnt
