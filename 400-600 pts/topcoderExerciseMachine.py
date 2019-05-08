#Problem Statement
#    
#You are writing firmware for an exercise machine. Each second, a routine in your firmware is called which decides whether it should display the percentage of the workout completed. The display does not have any ability to show decimal points, so the routine should only display a percentage if the second it is called results in a whole percentage of the total workout.
#Given a string time representing how long the workout lasts, in the format "hours:minutes:seconds", return the number of times a percentage will be displayed by the routine. The machine should never display 0% or 100%.
#Definition
#    
#Class:
#ExerciseMachine
#Method:
#getPercentages
#Parameters:
#string
#Returns:
#integer
#Method signature:
#def getPercentages(self, time):


#Gendo90 has submitted the 500-point problem for 150.00 points
#Successful on second try - had to learn about 'representation error'
# here: https://docs.python.org/2/tutorial/floatingpoint.html#representation-error

class ExerciseMachine(object):
    def getPercentages(self, time):
        hours, minutes, seconds = time.split(':')
        total_time_sec = int(seconds)+(int(minutes)*60)+(int(hours)*60*60)
        one_percent = total_time_sec/100.0
        print(one_percent)
        print(total_time_sec)

        count=0
        for second in range(1, total_time_sec):
            # have to account for representation error in the case '02:08:35'
            # for 60%
            eps=1.0e-10
            intended_num = round(second/one_percent)

            #if ((second/one_percent)-int(second/one_percent))<eps:
            if(abs((second/one_percent)-intended_num)<eps):
                print(second)
                count+=1

        return count


test = ExerciseMachine()

print(test.getPercentages('02:08:35'))
