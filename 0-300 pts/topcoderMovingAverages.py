# Problem Statement
#
# Moving averages are well known in stock charts analysis. They are used to emphasize the direction of a trend and to smooth out fluctuations. Athletes may use moving averages to analyze their training results.  Given a tuple (string) times containing the times from successive training sessions (e.g. the time to cycle a certain leg) and an integer n, return a tuple (integer) containing the n-moving averages in seconds for these times, with each average rounded down.  Each element of times is in the format "hh:mm:ss" (quotes for clarity), where hh, mm and ss are two digit numbers (with a leading zero if necessary) indicating the number of hours, minutes and seconds, respectively. A n-moving average is the average (i.e. the arithmetic mean) of n consecutive times. So for t times given, t-n+1 n-moving averages are to be calculated. The first average is composed from the times 1 to n, the second average from the times 2 to n+1 and so on, the last average is composed from the times t-n+1 to t.
# Definition
#
# Class:
# MovingAverages
# Method:
# calculate
# Parameters:
# tuple (string), integer
# Returns:
# tuple (integer)
# Method signature:
# def calculate(self, times, n):

#Gendo90 has submitted the 250-point problem for 202.94 points
#Successful on second try - had to change a for loop into a while loop due to
#modifying the "together" array
class MovingAverages(object):
    def calculate(self, times, n):
        t = 0
        averages = []
        while(t+n<=len(times)):
            total = 0
            for i in range(n):
                this_time = list(map(int, times[i+t].split(":")))
                this_time = this_time[2]+this_time[1]*60+this_time[0]*3600
                total+=this_time
            averages.append(int(total*1.0/n))
            t+=1


        return tuple(averages)


test = MovingAverages()

print(test.calculate(("01:19:10", "01:17:40", "01:19:44", "01:17:23", "01:17:07"), 3))
