# Problem Statement
#
# You have just finished eating your Chinese food, and the waiter has brought you the bill. You note the untaxed total on the bill, given as an integer in total. Additionally, you know the tax rate in your locale, given as an integer in taxPercent. Lastly, you have counted how much money you have, given as an integer in money.
# Since you feel the service was excellent, you want to give as large a tip as you can afford. You are to return the largest integral value of tip such that: total + floor(total*taxPercent/100) + floor(total*tip/100) <= money If there is no non-negative value of tip that satisfies the above inequality, return -1 (you don't have enough money to pay the bill and tax).
# Definition
#
# Class:
# WaiterTipping
# Method:
# maxPercent
# Parameters:
# integer, integer, integer
# Returns:
# integer
# Method signature:
# def maxPercent(self, total, taxPercent, money):


#Gendo90 has submitted the 250-point problem for 151.16 points
#got stuck on the "floor" issue - not simple rounding!
#Successful on first try!
class WaiterTipping(object):
    def maxPercent(self, total, taxPercent, money):
        comp_total = total + (total*1.0*taxPercent)//100
        tip_left = money-int(comp_total)
        print(tip_left)
        if(tip_left<0):
            return -1

        tip_perc = ((tip_left*100*1.0)/total)
        tip_perc_lower = int(tip_perc)
        tip_perc_higher = tip_perc_lower+1
        if(int(tip_perc_higher*total/100)<=tip_left):
            return tip_perc_higher
        else:
            return tip_perc_lower

test = WaiterTipping()

#workaround that is good to know about!
print(test.maxPercent(123, 52, 696))
# print(test.maxPercent(tuple(1), 20))
