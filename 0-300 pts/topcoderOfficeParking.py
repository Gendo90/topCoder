# Problem Statement
#
# The TopCoder office building is filled with very efficient people. Each of these people always parks their car in the closest (to the building) available parking space. The parking spaces are arranged linearly, with space number one being the closest to the building, space number two being the second closest to the building, etc.
# Given a sequence of employee arrivals and departures, determine the number of parking spaces used that day. The parking lot is empty at the beginning of the day. Names are case sensitive.
# For example in the sequence of events below:
# {"Alice arrives",
#  "bob arrives",
#  "Alice departs",
#  "Charles arrives",
#  "bob departs",
#  "Charles departs"}
#
# Alice parks in space 1
# bob parks in space 2
# Alice vacates space 1
# Charles parks in space 1
# bob vacates space 2
# Charles vacates space 1
# The total number of parking spaces used is 2.
# Definition
#
# Class:
# OfficeParking
# Method:
# spacesUsed
# Parameters:
# tuple (string)
# Returns:
# integer
# Method signature:
# def spacesUsed(self, events):

# Gendo90 has submitted the 300-point problem for 289.00 points
# Successful on first go!
class OfficeParking(object):
    def spacesUsed(self, events):
        curr_spaces = 0
        max_spaces = 0

        for i, event in enumerate(events):
            if(event.split(" ")[1]=="arrives"):
                curr_spaces+=1
            else:
                curr_spaces-=1
            if(curr_spaces>max_spaces):
                max_spaces=curr_spaces
        return max_spaces


test = OfficeParking()

print(test.spacesUsed())
