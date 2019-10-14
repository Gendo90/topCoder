# Problem Statement
#
# Your company is working on writing a piece of software to compress a text document. As part of the software development team, you have been asked to write a function that will find the longest repeated sub-string within a piece of text, such that the two chosen occurrences of the sub-string do not overlap. Your software is case sensitive, so two sub-strings are not the same if their capitalization differs. You have been instructed that, in a case where more than one such sub-string is the longest, the one that occurs earliest in the source string should be chosen.
# For instance, given the string "ABCDABCFG", the longest repeated sub-string is "ABC". In the string "ABABA", both "AB" and "BA" are repeated substrings, however, we choose "AB", since it occurs earlier. (Even though "ABA" appears twice as a sub-string, the two occurrences overlaps, so that can not be used.)
# You are given a string sourceText. You are to return a string that is the longest repeated sub-string. If more than one substring of equal maximum length is repeated, return the one that occurs first in the string. If no sub-string repeats itself, return "".
# Definition
#
# Class:
# TextCompressor
# Method:
# longestRepeat
# Parameters:
# string
# Returns:
# string
# Method signature:
# def longestRepeat(self, sourceText):


#Gendo90 has submitted the 250-point problem for 192.85 points
#Successful on first try!
#A little tricky to compare the strings, not the arrays - need to rejoin them!
class TextCompressor(object):
    def longestRepeat(self, sourceText):
        output = ""
        curr_ind = 0
        max_ind = len(sourceText)
        sourceText = [a for a in sourceText]
        while(curr_ind+len(output)<max_ind-len(output)):
            # print(curr_ind)
            while("".join(sourceText[curr_ind:curr_ind+len(output)+1]) in "".join(sourceText[curr_ind+len(output)+1:])):
                output=sourceText[curr_ind:curr_ind+len(output)+1]
            curr_ind+=1
        return "".join(output)

test = TextCompressor()

#workaround that is good to know about!
print(test.longestRepeat("ABABA"))
# print(test.longestRepeat(tuple(1), 20))
