"""
Given a number of tasks with a fixed service time. A task can only start when the task before it
completes. Arrange the tasks in such a way that the waiting time is minimum.

Input: list of service times
Output: min waiting time

Solution:
    The waiting can be reduced by finishing the tasks with smaller service time. Doing
    this will make the tasks with larger service times wait lesser.
TC: O(nlogn)
"""


def activity_selection(times):
    n = len(times)

    # sort the list of service times
    times.sort()

    return sum(t * (n - i - 1) for i, t in enumerate(times))


if __name__ == "__main__":
    times = [12, 5, 1, 2]
    print(activity_selection(times))
