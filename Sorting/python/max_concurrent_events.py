"""
Given a list of intervals (start_time, end_time), find the maximum number of events
happening concurrently.

Solution:
    Concurrent events at time t = (# started) - (# ended).
    Extract all endpoints and sort them by time. On a tie, a start comes before an end.

    TC: O(n log n)
    SC: O(2n), n: number of intervals
"""
from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int


@dataclass
class Endpoint:
    time: int
    is_start: bool


def max_concurrent_events(events):
    max_events = 0
    running_events = 0

    # first extract the endpoints
    endpoints = []
    for e in events:
        endpoints.append(Endpoint(e.start, True))   # start time endpoint
        endpoints.append(Endpoint(e.end, False))    # end time endpoint

    # sort by time; for equal times, start (key 0) comes before end (key 1)
    endpoints.sort(key=lambda ep: (ep.time, 0 if ep.is_start else 1))

    # +1 for every start, -1 for every end
    for ep in endpoints:
        running_events += 1 if ep.is_start else -1
        max_events = max(max_events, running_events)

    return max_events


if __name__ == "__main__":
    events = [Interval(*p) for p in [(1, 5), (6, 10), (11, 13), (14, 15), (2, 7), (4, 15),
                                     (8, 9), (13, 15), (18, 19)]]
    print(max_concurrent_events(events))
