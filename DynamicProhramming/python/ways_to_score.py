"""
Given a final score and scores for different moves/plays, find the no. of ways in
which that score can be achieved (combinations; order doesn't matter).

Solution:
    Very similar to climbing stairs problem.
    TC: O(sn), s: score and n: no. of play scores
"""


def ways_to_score_mem_helper(score, play_scores, cache):
    """(alternative memoized version from the original, commented out there)"""
    # when the score is reached
    if score == 0:
        return 1

    # when the result is not cached, compute
    if cache[score] == 0:
        # try all play scores which can help achieve current score
        i = 0
        while i < len(play_scores) and score - play_scores[i] >= 0:
            cache[score] += ways_to_score_mem_helper(score - play_scores[i], play_scores, cache)
            i += 1
    return cache[score]


def ways_to_score_mem(score, play_scores):
    cache = [0] * (score + 1)
    return ways_to_score_mem_helper(score, play_scores, cache)


def ways_to_score(final_score, play_scores):
    """finds the no. of ways a score can be achieved"""
    # each entry (i, j) stores the no. of ways in which score 'j' can be achieved
    # if play scores till 'i' in play_scores are allowed
    score_cmb = [[0] * (final_score + 1) for _ in range(len(play_scores))]

    # we start from bottom and go upto the top
    for i in range(len(play_scores)):
        # score of 0 can be achieved in 1 way by every play score
        score_cmb[i][0] = 1

        # find the ways for building 'j' score
        for j in range(1, final_score + 1):
            # we can either include the current play score or exclude it
            exclude_current_score = score_cmb[i - 1][j] if i >= 1 else 0
            include_current_score = score_cmb[i][j - play_scores[i]] if play_scores[i] <= j else 0

            score_cmb[i][j] = include_current_score + exclude_current_score
    return score_cmb[len(play_scores) - 1][final_score]


if __name__ == "__main__":
    play_scores = [1, 2, 3]
    score = 5
    print(ways_to_score(score, play_scores))
