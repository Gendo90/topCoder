# Problem Statement
#
# In soccer leagues, the winner of a match is awarded with 3 points and the loser 0 points. In case of a tie, both teams are awarded with 1 point each.
# Create a class Soccer containing the method maxPoints which takes a tuple (integer) wins, the number of wins for each team in the league, and a tuple (integer) ties, the number of ties for each team in the league and returns an integer, the maximum points a team in the league has. The i'th elements of wins and ties correspond to the number of wins and ties respectively for team i.
# Definition
#
# Class:
# Soccer
# Method:
# maxPoints
# Parameters:
# tuple (integer), tuple (integer)
# Returns:
# integer
# Method signature:
# def maxPoints(self, wins, ties):

#Gendo90 has submitted the 250-point problem for 244.08 points
#Successful on first try!
class Soccer(object):
    def maxPoints(self, wins, ties):
        together = zip(wins, ties)
        scores = []
        for team in together:
            wins = team[0]*3
            ties = team[1]*1
            scores.append(wins+ties)

        return max(scores)


test = Soccer()

print(test.maxPoints(533))
