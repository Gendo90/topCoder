# Problem Statement
#
# You are playing TopRPG, the latest and hottest new console-style RPG (role-playing game) to hit the market. Much like many RPGs, it features the main characters getting stronger as the game progresses by obtaining a nebulous sort of thing known as experience, which is typically acquired by killing monsters.
# The strategy guide open in front of you tells you how much experience you'll need to get to each level, represented as a tuple (integer) expNeeded. For example, if expNeeded were {150, 450, 900, 1800}, you would need a total of 150 experience to get to level 1 (from level 0), then another (450 - 150) = 300 experience to get to level 2, and so on.
# You have 0 experience at the start, and you are about to go through an area where you will get a fixed amount of experience. You want to know how far you will be from the next level after you finish. Given a tuple (integer) expNeeded, where the ith element is the total amount of experience required to advance to level i, and an int received, indicating the amount of experience you will get, return an int which is the amount of experience it will take you to get to the next level after you receive the experience.
# Definition
#
# Class:
# LevelUp
# Method:
# toNextLevel
# Parameters:
# tuple (integer), integer
# Returns:
# integer
# Method signature:
# def toNextLevel(self, expNeeded, received):

# Gendo90 has submitted the 250-point problem for 204.64 points
#Successful on first try!

class LevelUp(object):
    def toNextLevel(self, expNeeded, received):
        totalEXPNeeded = 0
        finalLevel = 0
        for i, level in enumerate(expNeeded):
            if(received<level):
                finalLevel = i
                break

        leftoverEXP = expNeeded[finalLevel]-received
        return leftoverEXP


test = LevelUp()

print(test.toNextLevel((150,450,900,1800), 133))
