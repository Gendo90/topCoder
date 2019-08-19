# Problem Statement
#
# You are to create a class Multiples with a method number, which takes three integers: min, max, and factor.
# Given a range of integers from min to max (inclusive), determine how many numbers within that range are evenly divisible by factor.
# Definition
#
# Class:
# Multiples
# Method:
# number
# Parameters:
# integer, integer, integer
# Returns:
# integer
# Method signature:
# def number(self, min, max, factor):

#Server not working for grading - invalid points (also does not accept my
#code as correct, although manually on my machine the test cases are valid - buggy...)
#Successful on first try!
class Multiples(object):
    def number(self, min, max, factor):
        total_divisible = 0

        for i in range(min, max+1):
            if(i*1.0%factor==0):
                total_divisible+=1

        return total_divisible





test = Multiples()

print(test.number(-1000000, 1000000, 1))
