"""
Given a text file which contains scores and student id in new line. So each record is there on a new line.
Find the top scoring student. Consider using only the top 3 scores for computing the avg., students with
at least 3 test scores are only considered.

Input: file
Output: string

Solution:
    Use a hash table for storing the student id and their scores.
    We use a priority queue of 3 elements as value for keys, whose creation is O(3)~O(1).
    After going through all the scores, we traverse through the table once and
    compute the avg, while keeping track of max.

    TC: O(n)
    SC: O(m), m: no. of distinct students, worst case: O(n), no. of scores = no. of students
"""
import heapq
import sys
from collections import defaultdict
from pathlib import Path


def find_student_with_highest_score(lines):
    # min-heap containing the top 3 scores for each student
    student_records = defaultdict(list)

    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue
        name, score = parts[0], int(parts[1])
        scores = student_records[name]
        heapq.heappush(scores, score)

        # keep only the top 3 scores
        if len(scores) > 3:
            heapq.heappop(scores)  # remove the smallest score at the top of the min-heap

    top_student = ""
    top_score = -1

    for name, scores in student_records.items():
        # student must have at least 3 scores
        if len(scores) == 3:
            curr_score = sum(scores)
            if curr_score > top_score:
                top_score = curr_score
                top_student = name

    return top_student


def _find_scores_file():
    here = Path(__file__).resolve().parent
    for p in (Path("scores.txt"), here / "scores.txt", here.parent / "scores.txt"):
        if p.is_file():
            return p
    return None


if __name__ == "__main__":
    path = _find_scores_file()
    if path is None:
        print("Could not open scores.txt", file=sys.stderr)
        sys.exit(1)

    with open(path) as f:
        student = find_student_with_highest_score(f)

    if not student:
        print("No student has at least 3 scores.")
    else:
        print(f"Top student: {student}")
