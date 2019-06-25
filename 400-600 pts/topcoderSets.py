# Problem Statement
#
# A set of numbers is a collection of numbers with no repeated elements. We can define the following set operations:
# The UNION of two sets A and B is a set containing all the elements that are either in A or in B.
# The INTERSECTION of two sets A and B is a set containing all the elements that are in both A and B.
# The SYMMETRIC DIFFERENCE of two sets A and B is a set containing all the elements that are either in A or in B, but not containing elements that are in both A and B.
# Given two tuple (integer)s representing sets A and B, and an operation applied on them, return a tuple (integer) representing the resulting set sorted in ascending order. If the result is an empty set then return an empty tuple (integer). operation will be one of the following: "UNION", "INTERSECTION", "SYMMETRIC DIFFERENCE".
# Definition
#
# Class:
# Sets
# Method:
# operate
# Parameters:
# tuple (integer), tuple (integer), string
# Returns:
# tuple (integer)
# Method signature:
# def operate(self, A, B, operation):

# Gendo90 has submitted the 500-point problem for 459.34 points
# Successful on first try! Easy if you knew there was already built-ins for
# sets!
class Sets(object):
    def operate(self, A, B, operation):
        setA = set(A)
        setB = set(B)
        if(operation=="UNION"):
            output = setA.union(setB)
        elif(operation=="INTERSECTION"):
            output = setA.intersection(setB)
        else:
            output = setA.symmetric_difference(setB)

        output = list(output)
        output.sort()

        return tuple(output)


test = Sets()

print(test.operate((1,2,3,4),
(3,4,5,6), "INTERSECTION"))
