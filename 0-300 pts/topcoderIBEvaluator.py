# Problem Statement
#
# For the International Baccalaureate (IB) diploma, students are assigned integer grades between 1 and 7 inclusive, based on exams taken at the end of high school. Unfortunately, these results are never available in time to assist universities with admissions decisions. To counteract this problem, IB teachers are required to predict in advance how well each student will perform on the exams. As these predictions can have an enormous impact on a student's future, schools are naturally very interested in evaluating their accuracy.
# Create a class IBEvaluator that contains a method getSummary, which is given a tuple (integer) predictedGrades and a tuple (integer) actualGrades. Corresponding elements in these arrays will represent the predicted and final grades, respectively, achieved by each student. The method should return a tuple (integer) with 7 elements, giving the percentage (rounded down) of predicted grades that differ from the actual grades by each value between 0 and 6 inclusive. Thus, element 0 of the return value should be the percentage of predictions that were correct, element 1 should be the percentage of predictions that differed by 1, etc.
# Definition
#
# Class:
# IBEvaluator
# Method:
# getSummary
# Parameters:
# tuple (integer), tuple (integer)
# Returns:
# tuple (integer)
# Method signature:
# def getSummary(self, predictedGrades, actualGrades):


#Gendo90 has submitted the 300-point problem for 269.77 points
#Successful on first try!
class IBEvaluator(object):
    def getSummary(self, predictedGrades, actualGrades):
        total_grades = len(actualGrades)
        num_grades_differ = [0 for i in range(7)]
        grades_together = zip(predictedGrades, actualGrades)
        for item in grades_together:
            ind = abs(item[0]-item[1])
            num_grades_differ[ind]+=1
        #convert to percentages
        num_grades_differ = [item*100/total_grades for item in num_grades_differ]
        output = [int(item) for item in num_grades_differ]

        return output



test = IBEvaluator()

print(test.getSummary((1,5,7,3), (3,5,4,5)))
