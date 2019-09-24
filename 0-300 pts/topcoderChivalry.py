# Problem Statement
#
# Two lines (or queues) of people often have to merge into a single-file line. But, chivalry is not dead! When a man and a woman are about to merge, the man will always let the woman go first.
# Given two lines of both men and women, write a method getOrder which will determine the genders of the people in the final line. If two women are at the front of both lines, the woman from the first line goes first. Likewise, if two men are at the front of both lines, the man from the first line goes first. Then, the people at the front of both lines are compared again.
# Each input line will be a string of letters, each one representing either a man or a woman. Each man will be represented by an 'M' and each woman by a 'W'. The output should be of the same form. The front of each line is the left-most character of the string.
# Definition
#
# Class:
# Chivalry
# Method:
# getOrder
# Parameters:
# string, string
# Returns:
# string
# Method signature:
# def getOrder(self, first, second):


#Gendo90 has submitted the 250-point problem for 174.68 points
#Successful on second try - missed the final elif condition "corner case"!
class Chivalry(object):
    def getOrder(self, first, second):
        first = [a for a in first]
        second = [b for b in second]
        output = []

        while(first or second):
            if(not first):
                output.extend(second)
                break
            elif(not second):
                output.extend(first)
                break
            elif(first[0]==second[0]):
                output.append(first.pop(0))
            elif(first[0]=="M" and second[0]=="W"):
                output.append(second.pop(0))
            elif(first[0]=="W" and second[0]=="M"):
                output.append(first.pop(0))

        return "".join(output)


test = Chivalry()

print(test.getOrder("MMMMMWWWW", "MWWWW"))
