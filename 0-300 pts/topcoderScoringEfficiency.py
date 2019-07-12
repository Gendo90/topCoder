# Problem Statement
#
# In basketball, players can attempt either two point or three point field goals, and if they are fouled, they can also attempt one point free throws. Since missing a free throw or a field goal often results in losing possession of the ball, it is important to make the most of each shot attempt. Traditionally, this efficiency has been measured by shooting percentage, which is defined as:
#                             Field goals made
#    Shooting percentage = ---------------------
#                          Field goals attempted
#  Unfortunately, this formula is problematic since it does not account for either free throws or the different types of field goals. Therefore, a new formula, called points per shot, is gaining prominence. This is given by:
#                                          Total points
#    Points per shot = -----------------------------------------------------
#                      (Field goals attempted) + 0.5*(Free throws attempted)
#  Consider, for example, a player that makes 4 of 5 two point field goals, 3 of 7 three point field goals, and 7 of 9 free throws. The player has earned 4*2 + 3*3 + 7*1 = 24 points with 5+7=12 field goal attempts and 9 free throw attempts. Thus, the player has earned 24/16.5 = 1.45454545... points per shot.
#
# Create a class ScoringEfficiency that contains a method getPointsPerShot, which is given a tuple (string) gameLog. This will give the history of one player's shot attempts, with each element being equal to one of the following strings (quotes for clarity):
# - "Made 2 point field goal"
# - "Missed 2 point field goal"
# - "Made 3 point field goal"
# - "Missed 3 point field goal"
# - "Made free throw"
# - "Missed free throw"
# Given this history, the method should return the player's points per shot, as computed above.
# Definition
#
# Class:
# ScoringEfficiency
# Method:
# getPointsPerShot
# Parameters:
# tuple (string)
# Returns:
# float
# Method signature:
# def getPointsPerShot(self, gameLog):

#Gendo90 has submitted the 250-point problem for 222.47 points
#Successful on first try!

class ScoringEfficiency(object):
    def getPointsPerShot(self, gameLog):
        total_points = 0
        shots_made = 0
        for item in gameLog:
            if("Made" in item):
                if("free" in item):
                    total_points+=1
                    shots_made+=0.5
                elif("2" in item):
                    total_points+=2
                    shots_made+=1
                else:
                    total_points+=3
                    shots_made+=1
            else:
                if("3" in item):
                    shots_made+=1
                elif("2" in item):
                    shots_made+=1
                else:
                    shots_made+=0.5
        pps = total_points*1.0/(shots_made)
        pps = round(pps, 9)
        return pps



test = ScoringEfficiency()

print(test.getPointsPerShot(("Made 3 point field goal",
 "Missed 2 point field goal")))
