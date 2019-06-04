# Problem Statement
#
# The inchworm is a creature of regular habits. She inches forward some distance along the branch of a tree, then stops to rest. If she has stopped at a leaf, she makes a meal of it. Then she inches forward the same distance as before, and repeats this routine until she has reached or passed the end of the branch.
# Consider an inchworm traveling the length of a branch whose leaves are spaced at uniform intervals. Depending on the distance between her resting points, the inchworm may or may not be able to eat all of the leaves. There is always a leaf at the beginning of the branch, which is where the inchworm rests before setting out on her journey.
# You are given three integer values that specify, in inches: the length of the branch; the distance traveled by the inchworm between rests; and the distance between each consecutive pair of leaves. Given that the inchworm only eats at rest, calculate the number of leaves she will consume.
# Definition
#
# Class:
# Inchworm
# Method:
# lunchtime
# Parameters:
# integer, integer, integer
# Returns:
# integer
# Method signature:
# def lunchtime(self, branch, rest, leaf):

# Gendo90 has submitted the 250-point problem for 194.73 points
#Successful on first try!
class Inchworm(object):
    def lunchtime(self, branch, rest, leaf):
        worm_position = 0
        num_eaten = 0

        for i in range(0, branch+1, rest):
            if((1.0*i)/leaf == int(i/leaf)):
                num_eaten+=1

        return num_eaten


test = Inchworm()

print(test.lunchtime(12, 6, 4))
