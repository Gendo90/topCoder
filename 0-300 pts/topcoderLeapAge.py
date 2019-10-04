# Problem Statement
#
# Your friend was born on "leap day" and has always been troubled by the fact that he just turned 24 this year on his 5th birthday. You would like to write him a nice program for his birthday to help him and other leap-day-born people keep track of how many birthdays they've had so far.
# You will be given two years as integers, year represents the current year and born represents the year the person was born. You are to return the number of leap days that have occurred in that time span, not including the first year if it is a leap year, but including the current year if it's a leap year.
# A leap year is any year that is a multiple of 4, unless it is divisible by 100 and not 400. For example, 1984 was a leap year, but 1900 wasn't, because it was divisible by 100 and not 400. 2000 was a leap year, because it was divisible by both 100 and 400.
# Definition
#
# Class:
# LeapAge
# Method:
# getAge
# Parameters:
# integer, integer
# Returns:
# integer
# Method signature:
# def getAge(self, year, born):


#Gendo90 has submitted the 250-point problem for 237.00 points
#Successful on first try!
class LeapAge(object):
    def getAge(self, year, born):
        years = range(born+1, year+1)
        days = 0;
        for a in years:
            if(a%4==0):
                if(a%100==0 and not a%400==0):
                    continue
                else:
                    days+=1
        return days

test = LeapAge()

#workaround that is good to know about!
print(test.getAge(123, 52, 696))
# print(test.getAge(tuple(1), 20))
