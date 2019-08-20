# Problem Statement
#
# You have acquired a list of the math and verbal test scores from all the children in the county. Write a class Average that contains a method belowAvg that takes two tuple (integer), math and verbal, representing the math and verbal scores of all of the children in the county, and returns the number of children who have a composite score which is below average in the county.
# The composite score is defined to be the sum of a child's math and verbal scores.
# Definition
#
# Class:
# Average
# Method:
# belowAvg
# Parameters:
# tuple (integer), tuple (integer)
# Returns:
# integer
# Method signature:
# def belowAvg(self, math, verbal):

#Gendo90 has submitted the 250-point problem for 237.57 points
#Successful on first try!
class Average(object):
    def belowAvg(self, math, verbal):
        if(isinstance(math, int)):
            return 0

        num_students = len(math)
        avg_math = sum(math)*1.0/num_students
        avg_verbal = sum(verbal)*1.0/num_students
        avg_composite = avg_math+avg_verbal
        together_score = zip(math, verbal)
        num_below_avg = 0
        for score in together_score:
            if(sum(score)<avg_composite):
                num_below_avg+=1

        return num_below_avg


test = Average()

print(test.belowAvg())
