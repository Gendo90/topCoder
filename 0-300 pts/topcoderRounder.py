# Problem Statement
#
# Most of the time when rounding a given number, it is customary to round to some multiple of a power of 10. However, there is no reason why we cannot use another multiple to do our rounding to. For example, you could round to the nearest multiple of 7, or the nearest multiple of 3.
# Given an integer n and an integer b, round n to the nearest value which is a multiple of b. If n is exactly halfway between two multiples of b, return the larger value.
# Definition
#
# Class:
# Rounder
# Method:
# round
# Parameters:
# integer, integer
# Returns:
# integer
# Method signature:
# def round(self, n, b):

#Gendo90 has submitted the 250-point problem for 235.45 points
#Successful on first try!
class Rounder(object):
    def round(self, n, b):
        before = 0
        next = b

        while(next<n):
            before = next
            next = next+b

        if(abs(next-n)<=abs(n-before)):
            return next
        else:
            return before



test = Rounder()

print(test.round(4, 10))
