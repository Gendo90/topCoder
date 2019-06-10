# Problem Statement
#
# When playing many classic role playing games you often write die rolls in the form "ndx", where n indicates the number of dice of size x to be rolled. A die of size x is an x-sided die that has a distinct number between 1 and x, inclusive, on each of its sides. For example, "2d8" would mean "roll two eight sided dice". Given a tuple (string) representing the dice to roll, return a tuple (integer) representing the minimum, maximum, and average die rolls (in that order). Round the value of the average die roll down to the highest integer less than or equal to the actual value. For example, the input {"1d8","3d4","2d6"} would have a minimum of 6 (if all the dice turned up ones), a maximum of 32 (if all the dice turned up their highest values), and an average of 19. The return value would be {6, 32, 19}.
# Definition
#
# Class:
# RPG
# Method:
# dieRolls
# Parameters:
# tuple (string)
# Returns:
# tuple (integer)
# Method signature:
# def dieRolls(self, dice):

# Gendo90 has submitted the 250-point problem for 160.31 points
# Successful on first try!
# Got interrupted by a phone call, otherwise would have been higher

class RPG(object):
    def dieRolls(self, dice):
        minimum = 0
        average = []
        combined_average = 0
        maximum = 0
        for dieSize in dice:
            diceValues = dieSize.split("d")
            # print(diceValues)
            numDice = int(diceValues[0])
            max_Die = int(diceValues[1])
            minimum += int(diceValues[0])
            thisAVG = (numDice, ((1+max_Die)/2.0))
            average.append(thisAVG)
            maximum += (numDice)*(max_Die)

        for numDice, avgVal in average:
            combined_average += numDice*(avgVal)

        return (minimum, maximum, int(combined_average))


test = RPG()

print(test.dieRolls(("3d4","1d6")))
