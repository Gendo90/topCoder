# Problem Statement
#
# A simple calculator accepts the following kinds of strings as input:
# 1) NUM+NUM
# 2) NUM-NUM
# 3) NUM*NUM
# 4) NUM/NUM
# where NUM is a positive integer, between 1 and 10000 inclusive that can contain leading zeros. Return the value produced by the given expression. Here +,-,*, and / denote addition, subtraction, multiplication and division respectively. All operations are done on integers, so "5/3" returns 1.
# Definition
#
# Class:
# SimpleCalculator
# Method:
# calculate
# Parameters:
# string
# Returns:
# integer
# Method signature:
# def calculate(self, input):

#Gendo90 has submitted the 250-point problem for 234.50 points
#Successful on first try!
class SimpleCalculator(object):
    def calculate(self, input):
        plus = input.split("+")
        minus = input.split("-")
        times = input.split("*")
        divided = input.split("/")

        if(len(plus)>1):
            output = int(plus[0])+int(plus[1])
            return int(output)
        elif(len(minus)>1):
            output = int(minus[0])-int(minus[1])
            return output
        elif(len(times)>1):
            output = int(times[0])*int(times[1])
            return output
        else:
            output = int(divided[0])/int(divided[1])
            return output



test = SimpleCalculator()

print(test.calculate())
