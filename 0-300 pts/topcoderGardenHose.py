# Problem Statement
#
# Our garden is a square containing plants in n rows and n columns, a total of n*n plants. The distance between plants within a row is rowDist and between plants within a column is colDist.
#
# I want to water the garden without getting my shoes muddy. That requires that I stand outside the garden, never closer than where the next row or column of the garden would be if it were enlarged. The hose can water plants that are hoseDist or less away from where I am standing. (Of course, I can move around and water from various locations.)
#
# Create a class GardenHose that contains the method countDead that takes n, rowDist, colDist, and hoseDist as inputs and returns the number of plants that cannot be watered.
# Definition
#
# Class:
# GardenHose
# Method:
# countDead
# Parameters:
# integer, integer, integer, integer
# Returns:
# integer
# Method signature:
# def countDead(self, n, rowDist, colDist, hoseDist):

# Gendo90 has submitted the 250-point problem for 117.50 points
#Successful on first try!
class GardenHose(object):
    def countDead(self, n, rowDist, colDist, hoseDist):
        total = n*n
        countRow = 0
        countCol = 0
        for i in range(1, hoseDist+1):
            if(i%rowDist==0):
                countRow+=1
            if(i%colDist==0):
                countCol+=1
            if(countRow>n//2 or countCol>n//2):
                return 0
        rowVal = (n-countRow*2)
        colVal = (n-countCol*2)
        print(rowVal, colVal)
        return rowVal*colVal


test = GardenHose()

print(test.countDead(3, 2, 1, 1))
