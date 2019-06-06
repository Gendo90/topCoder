# Problem Statement
#
# Prior to 1971, Britain used a system of coins that can be traced back to the time of Charlemagne. The three main units of coinage were the penny, the shilling, and the pound. There were 12 pennies in a shilling and 20 shillings in a pound. Given a number pence of pennies, convert this amount into pounds, shillings, and pennies by first converting as many pennies as possible into pounds, and then converting as many of the remaining pennies as possible into shillings. Return a tuple (integer) of size three containing the number of pounds, the number of shillings, and the number of pennies, in that order.
# Definition
#
# Class:
# BritishCoins
# Method:
# coins
# Parameters:
# integer
# Returns:
# tuple (integer)
# Method signature:
# def coins(self, pence):

# Gendo90 has submitted the 250-point problem for 240.30 points
#Successful on first try!
class BritishCoins(object):
    def coins(self, pence):
        pounds = pence//(12*20)
        reduced_pence = pence-(12*20*pounds)
        shillings = reduced_pence//(12)
        reduced_pence-=12*shillings

        return (pounds, shillings, reduced_pence)


test = BritishCoins()

print(test.coins(533))
