# Problem Statement
#
# You are searching for a new house. Location, location, location. You have identified a number of desirable attributes, and for each have sketched a rectangular area that contains all the locations that have that attribute.
# You want it all. You need to find the area that is contained in every one of your rectangles. Create a class Intersection that contains a method area that takes as input the collection of rectangles and returns the area of their common intersection.
# The collection of rectangles is given by a tuple (integer) x and a tuple (integer) y. The first two values of x and y specify opposing corners of one rectangle, the next two specify opposing corners of the next rectangle, etc. Thus, each rectangle is the region between its two x values and between its two y values.
# Definition
#
# Class:
# Intersect
# Method:
# area
# Parameters:
# tuple (integer), tuple (integer)
# Returns:
# integer
# Method signature:
# def area(self, x, y):

import numpy as np
# Gendo90 has submitted the 500-point problem for 197.69 points
# Successful on first try! Messed up by trying to use numpy, which topcoder
# did not support, and trying to get the set of all vertexes with nested for
# loops, which had too slow of a runtime for this case (400000000) and it
# would have been difficult to find the min and max x and y in that set, anyway
# The name just threw me - I should have drawn a picture!
class Intersect(object):
    def area(self, x, y):
        # x = np.reshape(x, (len(x)//2, 2))
        # y = np.reshape(y, (len(y)//2, 2))
        # together = zip(x, y)
        all_rects = []
        # print(x, y)
        x_min = min(x[0], x[1])
        x_max = max(x[0], x[1])
        y_min = min(y[0], y[1])
        y_max = max(y[0], y[1])
        if(len(x)>2):
            for i in range(2, len(x), 2):
                x_curr_min = min(x[i], x[i+1])
                x_curr_max = max(x[i], x[i+1])
                y_curr_min = min(y[i], y[i+1])
                y_curr_max = max(y[i], y[i+1])
                if(x_curr_min>x_min):
                    x_min = x_curr_min
                if(x_curr_max<x_max):
                    x_max = x_curr_max
                if(y_curr_min>y_min):
                    y_min = y_curr_min
                if(y_curr_max<y_max):
                    y_max = y_curr_max


        if(x_min>x_max or y_min>y_max):
            return 0
        else:
            output = (x_max-x_min)*(y_max-y_min)
            return output


test = Intersect()

print(test.area((10000,-10000),
(-10000,10000)))
