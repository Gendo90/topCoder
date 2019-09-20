# Problem Statement
#
# This task is about the scoring in the first phase of the die-game Yahtzee, where five dice are used. The score is determined by the values on the upward die faces after a roll. The player gets to choose a value, and all dice that show the chosen value are considered active. The score is simply the sum of values on active dice.
# Say, for instance, that a player ends up with the die faces showing 2, 2, 3, 5 and 4. Choosing the value two makes the dice showing 2 active and yields a score of 2 + 2 = 4, while choosing 5 makes the one die showing 5 active, yielding a score of 5.
# Your method will take as input a tuple (integer) toss, where each element represents the upward face of a die, and return the maximum possible score with these values.
# Definition
#
# Class:
# YahtzeeScore
# Method:
# maxPoints
# Parameters:
# tuple (integer)
# Returns:
# integer
# Method signature:
# def maxPoints(self, toss):


#Gendo90 has submitted the 250-point problem for 244.51 points
#Successful on first try!
class YahtzeeScore(object):
    def maxPoints(self, toss):
        output = []

        for item in toss:
            multiplier = toss.count(item)
            output.append(multiplier*item)

        return max(output)


test = YahtzeeScore()

print(test.maxPoints((2, 2, 3, 5, 4)))
