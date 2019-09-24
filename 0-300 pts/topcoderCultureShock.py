# Problem Statement
#
# Bob and Doug have recently moved from Canada to the United States, and they are confused by this strange letter, "ZEE". They need your assistance. Given a string text, replace every occurrence of the word, "ZEE", with the word, "ZED", and return the result.  Note that if "ZEE" is just part of a larger word (for example, "ZEES"), it should not be altered.
# Definition
#
# Class:
# CultureShock
# Method:
# translate
# Parameters:
# string
# Returns:
# string
# Method signature:
# def translate(self, text):


#Gendo90 has submitted the 250-point problem for 163.04 points
#Successful on second try - needed to split on spaces, not on a form of "ZEE"!
#Could be solved recursively
class CultureShock(object):
    def translate(self, text):
        test = text.split(" ")
        output = []
        for item in test:
            if (item=="ZEE"):
                output.append("ZED")
            else:
                output.append(item)

        return " ".join(output)


test = CultureShock()

print(test.translate("SWADSQ ZEB ZEE ZEE UNPUXDQKG ZEE ZEE ZEE"))
