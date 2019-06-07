# Problem Statement
#
# Note to plugin users: There is an image in the problem examples. Please use the applet to view it.
# After laser surgery, I was instructed to put drops in my eyes 6 times a day, spacing them as far apart as possible. Considering that I sleep for some period each day, it required some calculation to come up with an optimal schedule. Recognizing that I get similar instructions every time I get medication from the doctor, it became clear that a computer program was needed.
# Create a class EyeDrops that contains a method closest that is given sleepTime, the number of hours that the patient sleeps each day, and k, the number of doses required each day. The method returns the number of minutes between the closest doses, when the schedule is chosen to make this period as large as possible. You should assume that the patient sleeps for the same continuous period each day.
# The schedule that you choose will be applied for multiple days, so the period between closest doses may be between doses on different days.
# Definition
#
# Class:
# EyeDrops
# Method:
# closest
# Parameters:
# integer, integer
# Returns:
# float
# Method signature:
# def closest(self, sleepTime, k):

# Gendo90 has submitted the 300-point problem for 108.30 points
# Successful on second try - took a while to notice that the sleepTime needed
# to be multiplied by 60.0, and then had some extra stuff that was wrong in
# the if clause
class EyeDrops(object):
    def closest(self, sleepTime, k):
        if(k!=1):
            x = (24.0-sleepTime)/(k-1)
        else:
            return 24*60.0
        normal_sitch = (x)*60.0
        # print(normal_sitch)
        if((sleepTime*(60.0))<(normal_sitch)):
            x2 = (24.0)/(k)
            return x2*60.0

        return normal_sitch


test = EyeDrops()

print(test.closest(1, 7))
