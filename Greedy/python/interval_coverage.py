"""
Given a set of tasks with starting and ending time. Each task is represented as [start, end].
We can check the status of a task by visiting at any time within its closed interval, and that
visit also covers other tasks lying in that interval. Find the min number of visits needed
to cover all tasks.

Input: list of (start, end) tasks
Output: visit times (min number of visits)

Solution:
    Sort the tasks by end time. Visit at the end time of the first task; this covers every task
    that starts on or before it. Then pick the next task whose start isn't covered and visit at
    its end time. Repeat for the remaining tasks.

TC: O(nlogn)
"""


def calculate_min_visits(tasks):
    """Calculates the visits required for covering the entire set of tasks."""
    if not tasks:
        return []

    # sort the tasks by end time
    tasks.sort(key=lambda t: t[1])

    # first visit will be end time of first sorted task
    visits = [tasks[0][1]]

    for start, end in tasks[1:]:
        # if the current task starts after the last visit, it isn't covered,
        # so visit at the current task's end time
        if start > visits[-1]:
            visits.append(end)

    return visits


if __name__ == "__main__":
    tasks = [(2, 5), (3, 6), (1, 4), (7, 8)]
    visits = calculate_min_visits(tasks)
    print(" ".join(str(v) for v in visits))
