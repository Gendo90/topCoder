# Problem Statement
#
# A full-sized golf course consists of 18 lawns known as holes. The player's objective is to strike a ball with his club in such a way that it travels from a specified point at one end of the lawn to a specified point at the other, and to do so with as few strokes as he can. Associated with each hole is a positive number, the par, which is the number of strokes it is expected to take a competent golfer to complete the hole.
# A player's performance on an individual hole is described by a phrase that depends on the number of strokes he took relative to par. To make a "bogey", for example, means that the player has completed a hole in one stroke more than the par value, and a "double bogey" is two strokes over par. Two strokes under par, on the other hand, is an "eagle", while the "albatross", a rare bird indeed, is three strokes under par. The following is a complete dictionary of scoring phrases.
#
#     "triple bogey"  three strokes over par
#     "double bogey"  two strokes over par
#     "bogey"         one stroke over par
#     "par"           exactly par
#     "birdie"        one stroke under par
#     "eagle"         two strokes under par
#     "albatross"     three strokes under par
#     "hole in one"   exactly one stroke
# The managers of Gravel Mountain Golf Course have contracted you to implement a score-management system that will translate a single player's scores from the above jargon to a numerical total. You are given a tuple (integer) specifying the par value of each of the course's 18 holes in playing order. You are also given a tuple (string) such that the nth string describes the player's score on the nth hole. The reported scores will be valid and complete. Compute the player's total score and return it as an integer.
# Definition
#
# Class:
# GolfScore
# Method:
# tally
# Parameters:
# tuple (integer), tuple (string)
# Returns:
# integer
# Method signature:
# def tally(self, parValues, scoreSheet):

#Gendo90 has submitted the 250-point problem for 221.57 points
#Successful on first try!
class GolfScore(object):
    def tally(self, parValues, scoreSheet):
        comp_dict = {"triple bogey":3, "double bogey":2, "bogey":1, "par":0, "birdie":-1,
        "eagle":-2, "albatross":-3}
        together = zip(parValues, scoreSheet)
        total_score = 0
        for item in together:
            if(item[1] in comp_dict):
                total_score+=item[0]+comp_dict[item[1]]
            else:
                total_score+=1

        return total_score


test = GolfScore()

print(test.tally((1, 1, 1, 1, 1, 1,
 1, 1, 1, 5, 5, 5,
 5, 5, 5, 5, 5, 5), ("bogey", "bogey", "bogey", "bogey", "bogey", "bogey",
 "bogey", "bogey", "bogey", "eagle", "eagle", "eagle",
 "eagle", "eagle", "eagle", "eagle", "eagle", "eagle")))
