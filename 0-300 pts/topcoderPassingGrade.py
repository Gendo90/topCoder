# Problem Statement
#
# You are studying for the final exam in a tough course, and want to know how many points you need to score on the final to pass the course. You know how many points you earned on each assignment (pointsEarned), how many points were possible on each assignment (pointsPossible), and how many points are possible on the final exam (finalExam). You need to earn a minimum of 65% of the total possible points to pass the course. Assume your score on the final exam will be an integral number of points between 0 and finalExam, inclusive. Return the number of points you need to score on the final to pass the course, or -1 if it is impossible for you to pass the course.
# Definition
#
# Class:
# PassingGrade
# Method:
# pointsNeeded
# Parameters:
# tuple (integer), tuple (integer), integer
# Returns:
# integer
# Method signature:
# def pointsNeeded(self, pointsEarned, pointsPossible, finalExam):

#Gendo90 has submitted the 250-point problem for 188.41 points
#Successful on second try!
#Missed the final_points<0 edge condition (any score on final will pass!)

# import math

class PassingGrade(object):
    def pointsNeeded(self, pointsEarned, pointsPossible, finalExam):
        my_score = sum(pointsEarned)
        total_possible = sum(pointsPossible)
        final_points = 0.65*(finalExam+total_possible)-(my_score)
        if(int(final_points) != final_points):
            final_points = int(final_points)+1

        if(final_points>finalExam):
            return -1
        elif(final_points<0):
            return 0

        return final_points



test = PassingGrade()

print(test.pointsNeeded(800,118,5000,906,1500))
