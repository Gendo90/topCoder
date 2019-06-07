# Problem Statement
#
# You are climbing a staircase. The staircase consists of some number of flights of stairs separated by landings. A flight is a a continuous series of stairs from one landing to another. You are a reasonably tall athletic person, so you can climb a certain number of stairs in one stride. However, after each flight, there is a landing which you cannot skip because you need to turn around for the next flight (which continues in the opposite direction).
# You will be given the number of stairs in each flight in a tuple (integer) flights. Element 0 of flights represents the number of stairs in the first flight, element 1 is the number of stairs in the second flight, etc. You will also be given an integer stairsPerStride, which is how many continuous stairs you climb in each stride. If it takes two strides to turn around at a landing, return the number of strides to get to the top of the staircase. You do not need to turn at the top of the staircase.
# Definition
#
# Class:
# StairClimb
# Method:
# stridesTaken
# Parameters:
# tuple (integer), integer
# Returns:
# integer
# Method signature:
# def stridesTaken(self, flights, stairsPerStride):

# Gendo90 has submitted the 250-point problem for 233.70 points
# Successful on first try!
class StairClimb(object):
    def stridesTaken(self, flights, stairsPerStride):
        stridesTotal = 0
        for i, stairway in enumerate(flights):
            stridesTotal+= stairway//stairsPerStride
            if(stairway%stairsPerStride!=0):
                stridesTotal+=1

            # Do not turn around on landing if last stairway
            if(i!=len(flights)-1):
                stridesTotal+=2 #turn around on landing

        return stridesTotal

test = StairClimb()

print(test.stridesTaken((15, 15)))
