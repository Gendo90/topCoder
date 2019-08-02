# Problem Statement
#
# Given a string, input, with up to 50 characters, find the length of the longest substring that appears at least twice (non-overlapping) in input. If no substring appears twice, non-overlapping, return 0.
# Strings are case sensitive, and only upper case letters and lower case letters are allowed in input.
# For example, in the string "ABCDEXXXYYYZZZABCDEZZZYYYXXX" the longest substring which appears at least twice is "ABCDE". These two substrings do not overlap so you would return 5.
# Definition
#
# Class:
# Reppity
# Method:
# longestRep
# Parameters:
# string
# Returns:
# integer
# Method signature:
# def longestRep(self, input):

#Gendo90 has submitted the 250-point problem for 215.83 points
#Successful on first try!
class Reppity(object):
    def longestRep(self, input):
        longest = 0
        for ind in range(len(input)):
            currLen = 0
            thisStr = ""
            while(input.find(input[ind:ind+currLen+1], ind+currLen+1)!=-1):
                currLen+=1
            thisStr = input[ind:ind+currLen]
            # print(thisStr)
            if(len(thisStr)>=longest):
                longest = len(thisStr)

        return longest


test = Reppity()

print(test.longestRep("abcdabcdabcdabCD"))
