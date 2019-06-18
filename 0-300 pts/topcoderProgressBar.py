# Problem Statement
#
# Installation programs often run several tasks, one after another. Each task is assigned an integer, the expected execution time of this task. During the installation, a progress bar shows the user what percentage of the installation time has elapsed. In this problem, the bar will be represented by a string containing exactly 20 characters. If X% of the installation has been completed, then the leftmost X% of these characters should be a '#', while the remaining characters should be '.'. If necessary, round down the number of '#' characters to the nearest integer less than or equal to the actual value (see example 0). The bar starts at 0% and is only updated each time a task finishes execution.
# Create a class ProgressBar containing the method showProgress which takes a tuple (integer) taskTimes, the expected execution time for each task in the order they are run, and an integer tasksCompleted, the number of these tasks that have been completed. The method should return a string containing exactly 20 characters showing the progress bar according to the descriptions above.
# Definition
#
# Class:
# ProgressBar
# Method:
# showProgress
# Parameters:
# tuple (integer), integer
# Returns:
# string
# Method signature:
# def showProgress(self, taskTimes, tasksCompleted):

#Gendo90 has submitted the 250-point problem for 225.14 points
#Successful on first try!
class ProgressBar(object):
    def showProgress(self, taskTimes, tasksCompleted):
        total_time = sum(taskTimes)
        task_comp_time = sum(taskTimes[i] for i in range(tasksCompleted))
        percent_time = int((task_comp_time/total_time)*100)
        num_pounds = percent_time//5
        num_dots = 20-num_pounds

        output = "#"*num_pounds+"."*num_dots

        return output


test = ProgressBar()

print(test.showProgress((19,6,23,17), 3))
