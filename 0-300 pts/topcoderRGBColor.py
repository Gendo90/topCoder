# Problem Statement
#
# When doing any work with visual media it is often very useful to have the complement of a color on hand to create contrast and bring the focus of a picture to a particular place. To create the complement of a color on a computer, each of the red, green, and blue values of a color are inverted. Each of the red, green, and blue values of a color can range from 0 to 255, inclusive. If a particular component of one color is 50, then that component of its complement is 255-50=205.  Although this generally works well, it doesn't generate good complements for grey colors that have all three components right around 128. To fix this you will return an alternate complement for grey colors. If each component of a color and its corresponding component of the color's complement differ by 32 or less, then make the complement of each component by either adding 128 to a component's value, or by subtracting 128 from a component's value, whichever one results in a legal value. For example, the color {120,130,140} would have the complement {125,105,115}, but each component in the color and the complement differ by 32 or less, so we make the complement {248,2,12}.  Create a class RGBColor with a method getComplement that takes a tuple (integer) rgb representing the red, green, and blue values of a color, in that order, and returns a tuple (integer) representing the red, green, and blue values of the complement of that color, in that same order.
# Definition
#
# Class:
# RGBColor
# Method:
# getComplement
# Parameters:
# tuple (integer)
# Returns:
# tuple (integer)
# Method signature:
# def getComplement(self, rgb):
#
#Gendo90 has submitted the 250-point problem for 190.96 points
#Successful on second try - missed an equals sign for item-128>0
#Will need to check output range better next time!
class RGBColor(object):
    def getComplement(self, rgb):
        normal_complement = [255-a for a in rgb]

        greyArray = []

        for i, item in enumerate(normal_complement):
            if(abs(item-rgb[i])<=32):
                greyArray.append(True)

        final_output = []

        if(len(greyArray)==3):
            for item in rgb:
                if(item-128>=0):
                    final_output.append(item-128)
                else:
                    final_output.append(item+128)
        else:
            final_output=normal_complement

        return tuple(final_output)


test = Stairs()

print(test.designs((25, 25, 60, 100)))
