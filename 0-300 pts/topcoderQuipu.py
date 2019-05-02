#Problem Statement
#    
#The Incas used a sophisticated system of record keeping consisting of bundles of knotted cords. Such a bundle of cords is called a quipu. Each individual cord represents a single number. Surprisingly, the Incas used a base-10 positional system, just like we do today. Each digit of a number is represented by a cluster of adjacent knots, with spaces between neighboring clusters. The digit is determined by the number of knots in the cluster. For example, the number 243 would be represented by a #cord with knots tied in the following pattern#
#     -XX-XXXX-XXX-
#where each uppercase 'X' represents a knot and each '-' represents an unknotted segment of cord (all quotes for clarity only).
#Unlike many ancient civilizations, the Incas were aware of the concept of zero, and used it in their quipus. A zero is represented by a cluster containing no knots. For example, the number 204003 would be represented by a cord with knots tied in the following pattern
#     -XX--XXXX---XXX-
#        ^^    ^^^
#        ^^    ^^^
#        ^^    two zeros between these three segments
#        ^^
#        one zero between these two segments
#Notice how adjacent dashes signal the presence of a zero.
#Your task is to translate a single quipu cord into an integer. The cord will be given as a string knots containing only the characters 'X' and '-'. There will be a single '-' between each cluster of 'X's, as well as a leading '-' and a trailing '-'. The first cluster will not be empty.
#Definition
#    
#Class:
#Quipu
#Method:
#readKnots
#Parameters:
#string
#Returns:
#integer
#Method signature:
#def readKnots(self, knots):

#Gendo90 has submitted the 250-point problem for 194.56 points
#Successful on first try!

#Successful on first try!
class Quipu(object):
    def readKnots(self, knots):
        split_segments = knots.split('-')
        #remove leading and trailing edge parts
        split_segments.pop()
        split_segments.pop(0)
        print(split_segments)

        num = [str(len(item)) for item in split_segments]
        value = ''.join(num)

        return value


test = Quipu()

print(test.readKnots('-XX--XXXX-XXX-'))
