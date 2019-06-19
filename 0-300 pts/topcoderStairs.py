# Problem Statement
#
# A set of stairs consists of risers (the vertical parts of the stairs) and treads (the horizontal parts that you walk on). The stairs alternate treads and risers, starting and ending with a riser as shown below.
# A set of stairs with two treads would have three risers and would look similar to this picture:
#
#                 +........
#                 |
#             +---+
#             |
#         +---+
#         |
# ........+
# We have the following requirements for a set of stairs:
# all risers must have the same integer height
# all treads must have the same integer width
# each riser must be less than or equal to maxHeight
# each tread must be greater than or equal to minWidth
# The totalWidth of the stairs is the sum of all the tread widths, while the totalHeight of the stairs is the sum of all the riser heights. The stairs start with a riser and end with a riser.
# Create a class Stairs that contains a method designs that takes as input four integers: maxHeight, minWidth, totalHeight, totalWidth. It returns the number of different designs that meet the design criteria.

#Gendo90 has submitted the 250-point problem for 122.40 points
#Successful on third try - made a careless error with the maxHeight+1 needed
#for the range, because the upper bound is exclusive...
    pass
class Stairs(object):
    def designs(self, maxHeight, minWidth, totalHeight, totalWidth):
        design_count = 0

        for height in range(1, maxHeight+1):
            riser_count = totalHeight/height
            if(riser_count!=int(riser_count)):
                continue
            tread_count = riser_count-1
            if(tread_count*minWidth<=totalWidth and tread_count!=0):
                tread_width = totalWidth/tread_count
                if(tread_width==int(tread_width)):
                    design_count+=1

        return design_count


test = Stairs()

print(test.designs(1, 2, 3, 4))
