# Problem Statement
#
# In the new boardgame Medici, you play an aristocrat in 15th-century Florence. On each turn, you gather points in three categories: fame, fortune, and dirty secrets with which you can blackmail other players. The winner is the player with the most points in his weakest category at the end of the game. For example, suppose there are three players with the following points:
#     NAME       FAME  FORTUNE  SECRETS
#     ---------------------------------
#     Salvestro   20      60       40
#     Giovanni    30      80       30
#     Cosimo      50      40       50
# Salvestro's weakest category is Fame, in which he has 20 points. Giovanni's weakest categories are Fame and Secrets, with 30 points in both. Cosimo's weakest category is Fortune, with 40 points. Cosimo is the winner.
# You will be given three tuple (integer)s, fame, fortune, and secrets. The points for player i are given as the i-th elements of the three tuple (integer)s. You are to return the (zero-based) index of the winning player. If there is a tie for the winning score, the game is declared a draw and replayed, in which case you should return -1.
# Definition
#
# Class:
# Medici
# Method:
# winner
# Parameters:
# tuple (integer), tuple (integer), tuple (integer)
# Returns:
# integer
# Method signature:
# def winner(self, fame, fortune, secrets):

#Gendo90 has submitted the 250-point problem for 181.70 points
#took some time to get the zip function correct for 3 (not 2!) items
#Successful on first try!
class Medici(object):
    def winner(self, fame, fortune, secrets):
        fame = list(fame)
        fortune = list(fortune)
        secrets = list(secrets)
        scores = zip(fame, fortune, secrets)
        # print(scores)
        min_for_players = []
        for player in scores:
            min_for_players.append(min(player))

        best = max(min_for_players)
        # print(min_for_players)
        this_winner = min_for_players.index(best)

        if((this_winner+1)<len(min_for_players) and best in min_for_players[this_winner+1:]):
            return -1
        else:
            return this_winner




test = Medici()

print(test.winner((1, 0), (1, 99), (1, 99)))
