# Problem Statement
#
# The least common multiple of a group of integers is the smallest number that can be evenly divided by all the integers in the group. Given two ints, first and last, find the least common multiple of all the numbers between first and last, inclusive.
# Definition
#
# Class:
# LCMRange
# Method:
# lcm
# Parameters:
# integer, integer
# Returns:
# integer
# Method signature:
# def lcm(self, first, last):

# Gendo90 has submitted the 250-point problem for 222.52 points
#Successful on first try!
class LCMRange(object):
    def lcm(self, first, last):
        nums_list = range(first, last+1)

        i=1
        while(True):
            lcm_case = True
            for index, item in enumerate(nums_list):
                if(not i%item==0):
                    break
                elif(index==len(nums_list)-1):
                    return i
            i+=1

        return i


test = LCMRange()

print(test.lcm(1, 5))
