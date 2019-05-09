#Problem Statement
#    
#Given the width and height of a rectangular grid, return the total number of rectangles (NOT counting squares) that can be found on this grid.
#For example, width = 3, height = 3 (see diagram below):
# __ __ __
#|__|__|__|
#|__|__|__|
#|__|__|__|
#In this grid, there are 4 2x3 rectangles, 6 1x3 rectangles and 12 1x2 rectangles. Thus there is a total of 4 + 6 + 12 = 22 rectangles. Note we don't count 1x1, 2x2 and 3x3 rectangles because they are squares.
#Definition
#    
#Class:
#RectangularGrid
#Method:
#countRectangles
#Parameters:
#integer, integer
#Returns:
#long integer
#Method signature:
#def countRectangles(self, width, height):


# Gendo90 has submitted the 500-point problem for 157.36 points
# Successful on first try, but took a while to see the pattern
# Should not have looked at single-row examples and tried to build it from that,
# since it worked initially and then broke down later...

class RectangularGrid(object):
    def countRectangles(self, width, height):
        count = 0
        # need to include 2x3 in a 4x4 matrix, for example
        # only account for 1xn and nx(height or width)
        test_width = width
        test_height = height
        #print(count)
        while(test_width>0):
            width_mult = width-test_width+1
            test_height = height
            while(test_height>0):
                height_mult = height-test_height+1
                total_mult = width_mult*height_mult
                if(test_width!=test_height):
                    count+=total_mult
                test_height-=1
            test_width-=1

        return count


test = RectangularGrid()

print(test.countRectangles(10, 10))
