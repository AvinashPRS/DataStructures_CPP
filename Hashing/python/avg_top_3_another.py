"""
Alternative version of avg_top_3_scores: find the top scoring student using the sum of
their top 3 scores (only students with at least 3 scores are considered).

Uses a dict of min-heaps (heapq), each capped at 3 elements.
"""
import heapq
from pathlib import Path


def find_student_with_highest_score(lines):
    student_records = {}

    # make the student score record hash table
    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue
        name, score = parts[0], int(parts[1])
        heap = student_records.setdefault(name, [])
        heapq.heappush(heap, score)
        # if there are more than 3 scores, remove the smallest
        if len(heap) > 3:
            heapq.heappop(heap)

    # find the top scoring student
    top_student = ""
    top_score = 0

    for name, heap in student_records.items():
        # reset curr_score for each student
        if len(heap) == 3:
            curr_score = sum(heap)
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
        raise SystemExit("Could not open scores.txt")
    with open(path) as f:
        print("Top student:", find_student_with_highest_score(f))
