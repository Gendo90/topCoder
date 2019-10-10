# Problem Statement
#
# You will be given a string str consisting of lowercase letters. You will return a tuple (string) containing elements x and y in that order. The returned strings x and y must satisfy:
# 1) The string xy (x with y concatenated on the end) must equal str.
# 2) The number of a's in x must equal the number of b's in y.
# 3) If multiple solutions are possible, use the one that maximizes the length of x.
# See the examples for further clarifications.
# Definition
#
# Class:
# EqualSubstrings
# Method:
# getSubstrings
# Parameters:
# string
# Returns:
# tuple (string)
# Method signature:
# def getSubstrings(self, str):


#Gendo90 has submitted the 250-point problem for 228.34 points
#Successful on first try!
#A little tricky to understand!
class EqualSubstrings(object):
    def getSubstrings(self, str):
        x = [s for s in str]
        y = []
        while(x.count("a")!=y.count("b")):
            y.insert(0, x.pop())

        output_x = "".join(x)
        output_y = "".join(y)

        return (output_x, output_y)

test = EqualSubstrings()

#workaround that is good to know about!
print(test.getSubstrings("bbbbbb"))
# print(test.getSubstrings(tuple(1), 20))
