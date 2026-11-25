"""
Given a set of tasks, each requiring a fixed time. Each worker does exactly two tasks. Assign the
tasks such that all the tasks complete in the least amount of time.

Input: list of service times
Output: assignment of tasks with min completion time

Solution:
    Pairing long tasks together makes the total time larger, so pair each large task
    with a small task.

TC: O(nlogn)
"""


def min_time_arrangement(tasks):
    """Finds the minimum time consuming arrangement of tasks."""
    if not tasks:
        return []

    # sort the tasks
    tasks.sort()

    # pair the largest with the smallest
    n = len(tasks)
    return [(tasks[i], tasks[n - 1 - i]) for i in range(n // 2)]


if __name__ == "__main__":
    tasks = [5, 22, 1, 16, 4, 44]
    for first, second in min_time_arrangement(tasks):
        print(f"{first}, {second}")
