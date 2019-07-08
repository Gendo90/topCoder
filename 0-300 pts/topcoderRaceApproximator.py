# Problem Statement
#
# If a runner races a distance D in time T, and later races a distance 2D, that runner will likely take more than 2T time to finish it. An examination of how times change with distances for a given runner can lead to the following approximation for the time it will take that runner to finish a given distance. Given two races with distances D1 and D2 which a runner ran in times T1 and T2, respectively, the approximate time it will take a runner to run a distance D is given by: T1*e^(ln(T2/T1)*ln(D1/D)/ln(D1/D2)).  When you race it is nice to have a time in mind that you'd like to be able to finish your race in. You are somewhat new to running and have only run two races of different distances. You are running a third race soon, and you want to use this equation to give you an estimate of how fast you should run. Since your upcoming race is a distance that falls between your first and second races' distances, you know this approximation will probably be fairly accurate. Create a class RaceApproximator with a method timeToBeat that takes integers d1, t1, d2, t2, and raceDistance, and returns a string that is the time you should be able to run in your upcoming race. d1, t1, d2 and t2 represent your shorter race's distance, your time in that race, your longer race's distance, and your time in that race, respectively. raceDistance is the distance of your upcoming race. All distances are in meters and all times are in seconds. Your return value should be truncated to an integer value, and formatted as "h:mm:ss" (all quotes are for clarity only) with"h" being the number of hours, "mm" being the number of minutes, and "ss" being the number of seconds.
# Definition
#
# Class:
# RaceApproximator
# Method:
# timeToBeat
# Parameters:
# integer, integer, integer, integer, integer
# Returns:
# string
# Method signature:
# def timeToBeat(self, d1, t1, d2, t2, raceDistance):

#Gendo90 has submitted the 250-point problem for 180.94 points
#Successful on first try!
#Not bad considering I did not know the exp and log functions that well!

import math

class RaceApproximator(object):
    def timeToBeat(self, d1, t1, d2, t2, raceDistance):
        tx = t1*math.exp(math.log(t2/t1)*math.log(d1/raceDistance)/(math.log(d1/d2)))

        h = tx//(60**2)
        h = int(h)
        tx -= h*(60**2)
        mm = tx//(60)
        mm = int(mm)
        tx -= mm*60
        ss = int(tx)

        h = str(h)
        if(len(str(mm))!=2):
            mm = "0"+str(mm)
        else:
            mm = str(mm)

        if(len(str(ss))!=2):
            ss = "0"+str(ss)
        else:
            ss = str(ss)

        output = h+":"+mm+":"+ss

        return output



test = RaceApproximator()

print(test.timeToBeat(800,118,5000,906,1500))
