"""Select the maximum number of non-overlapping activities."""
import sys
from dataclasses import dataclass


@dataclass
class Activity:
    id: int
    start_time: int
    end_time: int


def handle_error():
    print("Error occured ")
    sys.exit(1)


def activity_selection(a):
    """
    a: list of activities, where each activity has a start time and end time.
       Should have >= 1 element. The list is sorted in place by end time.
    Return value: list of indexes (into the sorted list) of the selected activities
    """
    # Sort the activities in non-decreasing order of their end time
    a.sort(key=lambda act: act.end_time)

    # Keep a track of the current time as we process the activities
    cur_time = 0
    selected = []
    for i, act in enumerate(a):
        # Pick the activity whose start time is on or after current time
        if act.start_time >= cur_time:
            selected.append(i)
            # Update the current time to the end time of the activity
            cur_time = act.end_time

    return selected


def run_test(a, expected_result):
    selected = activity_selection(a)

    for index in selected:
        print(f"Perform Activity {a[index].id}: Start time = {a[index].start_time}, "
              f"End time = {a[index].end_time}")

    if len(selected) != expected_result:
        handle_error()

    print("__________________________________")


def test_01():
    a = [Activity(1000, 0, 5), Activity(1001, 1, 2), Activity(1002, 3, 6)]
    run_test(a, 2)


def test_02():
    a = [Activity(1000, 0, 1), Activity(1002, 1, 5), Activity(1001, 2, 3), Activity(1003, 4, 7)]
    run_test(a, 3)


if __name__ == "__main__":
    test_01()
    test_02()
    print("Test passed")
