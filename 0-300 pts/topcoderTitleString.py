# Problem Statement
#
# A common word-processing task is capitalizing the first letter of each word in a title. Write a class TitleString with a method toFirstUpperCase that takes a string title containing lowercase words separated by one or more space characters and returns a string that is identical to title except with the first character of each word capitalized.
# Definition
#
# Class:
# TitleString
# Method:
# toFirstUpperCase
# Parameters:
# string
# Returns:
# string
# Method signature:
# def toFirstUpperCase(self, title):


#Gendo90 has submitted the 250-point problem for 240.12 points
#Successful on first try!
class TitleString(object):
    def toFirstUpperCase(self, title):
        words = title.split(" ")
        output = [word.capitalize() for word in words]

        output = " ".join(output)


        return output


test = TitleString()

print(test.toFirstUpperCase("  lord of the rings   the fellowship of the ring  "))
