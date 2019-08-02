# Problem Statement
#
# The definition of how to multiply a string by an integer follows:
# The empty string ("") multiplied by any integer is the empty string (""). For example: "" * 9 = ""
# Any string multiplied by 0 is the empty string (""). For example: "Terrific" * 0 = ""
# A non-empty string S multiplied by a positive integer k is the concatenation of k occurrences of S. For example: "Great" * 4 = "GreatGreatGreatGreat"
# A non-empty string S multiplied by a negative integer k is the concatenation of k occurrences of the reverse of S. For example: "Great" * -4 = "taerGtaerGtaerGtaerG"
# Your method will take a string and an integer and return their product.
# Definition
#
# Class:
# StringMult
# Method:
# times
# Parameters:
# string, integer
# Returns:
# string
# Method signature:
# def times(self, sFactor, iFactor):

#Gendo90 has submitted the 250-point problem for 237.11 points
#Successful on first try!
class StringMult(object):
    def times(self, sFactor, iFactor):
        if(len(sFactor)==0 or iFactor==0):
            return ""
        elif(iFactor>0):
            return sFactor*iFactor
        else:
            return (sFactor[::-1])*(-iFactor)



test = StringMult()

print(test.times("AbC", -3))
