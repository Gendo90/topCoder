# Problem Statement
#
# Even students who hate math find one calculation very useful -- what is the lowest score I can get on the last test and pull out a certain grade? Let's write a program to help them minimize their education.
# We will assume that an average score of 90 or higher is rewarded with an A grade, 80 or higher (but less than 90) is a B, 70 or higher (but less than 80) is a C, 60 or higher (but less than 70) is a D. All test scores are integers between 0 and 100 inclusive and the average is NOT rounded -- for example an average of 89.99 does NOT get you an A.
# Create a class Education that contains a method minimize that is given a string desire indicating the desired grade and a tuple (integer) tests containing the scores on all but the final test. The method returns the lowest possible test score for the final test that will earn at least the desired grade. If even a perfect score won't get the desired grade, return -1.
# The desired grade will be given as a string of length 1, either "A", "B", "C", or "D".
# Definition
#
# Class:
# Education
# Method:
# minimize
# Parameters:
# string, tuple (integer)
# Returns:
# integer
# Method signature:
# def minimize(self, desire, tests):

#Gendo90 has submitted the 250-point problem for 225.77 points
#Successful on first try!
class Education(object):
    def minimize(self, desire, tests):
        score_map = {"A": 90, "B": 80, "C": 70, "D": 60}
        desired_score = score_map[desire]

        total_tests = len(tests)
        total_scores = sum(tests)
        needed_score = (desired_score)*(total_tests+1)-total_scores

        if(needed_score<=0):
            return 0

        if(int(needed_score)!=needed_score):
            needed_score = int(needed_score)+1

        if(needed_score<=100):
            return needed_score

        return -1



test = Education()

print(test.minimize("A", (0, 70)))
