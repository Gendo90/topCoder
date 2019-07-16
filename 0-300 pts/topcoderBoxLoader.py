import itertools
# Problem Statement
#
# Your company has a new box loading robot. It is your job to program it to pack items into the shipping boxes. The robot does not have a very large program memory so you are restricted to placing all the items into the boxes in the same orientation. Each item is a rectangular solid with dimensions itemX by itemY by itemZ. The box is also rectangular with the dimensions boxX by boxY by boxZ. The items can be placed in the box in any orthogonal orientation (ie. the sides of the items must be parallel to the sides of the box), but only whole items can be placed in the box. Your task here is to determine the greatest number of items that can be packed into the box (with all the items in the same orientation).
# For example, if the box is 100x98x81 units and the items are 3x5x7 units, then orienting the items so they are 5x7x3, allows them to fit in the box in a 20x14x27 grid, filling the entire box, which is optimal: 7560 items.
# Definition
#
# Class:
# BoxLoader
# Method:
# mostItems
# Parameters:
# integer, integer, integer, integer, integer, integer
# Returns:
# integer
# Method signature:
# def mostItems(self, boxX, boxY, boxZ, itemX, itemY, itemZ):

#Gendo90 has submitted the 250-point problem for 185.71 points
#Successful on first try!
#Would have gotten it sooner if I had known more about itertools.permutations!

class BoxLoader(object):
    def mostItems(self, boxX, boxY, boxZ, itemX, itemY, itemZ):
        box_dim = [boxX, boxY, boxZ]
        item_dim = [itemX, itemY, itemZ]
        num_fit_total = 0

        all_item_dim_possible = itertools.permutations(item_dim)
        for item in all_item_dim_possible:
            xTotal = boxX//item[0]
            yTotal = boxY//item[1]
            zTotal = boxZ//item[2]
            new_total_fit = xTotal*yTotal*zTotal
            if(new_total_fit>num_fit_total):
                num_fit_total=new_total_fit

        return num_fit_total



test = BoxLoader()

print(test.mostItems(100, 98, 81, 3, 5, 7))
