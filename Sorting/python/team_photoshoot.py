"""
Given heights of players of two teams (same size), check whether one team can stand
in a row behind the other such that every player is taller than the one in front.

Solution:
    Sort both teams; then the i-th tallest of the back team must be taller than the
    i-th tallest of the front team for every i.

    TC: O(n log n)
"""


def can_team_be_placed(team1, team2):
    """Checks if team1 can be placed behind team2."""
    team1 = sorted(team1)
    team2 = sorted(team2)

    for i in range(len(team1) - 1, -1, -1):
        # if team1's player is shorter, it's not possible
        if team1[i] < team2[i]:
            return False
    return True


if __name__ == "__main__":
    team1 = [1.8, 1.8, 1.9, 2.1, 2.2]
    team2 = [1.2, 2.1, 1.6, 1.8, 1.7]

    print(int(can_team_be_placed(team1, team2) or can_team_be_placed(team2, team1)))
