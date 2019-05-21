# Problem Statement
#
# You are looking for a place to park your car on a suburban street. You can park at any position that meets the following requirements:
# 1.	It is not directly in front of a private driveway.
# 2.	It is not directly in front of a bus stop.
# 3.	It is not 5 meters before a bus stop.
# 4.	It is not 10 meters before a bus stop.
# 5.	It is not directly in front of a side-street.
# 6.	It is not 5 meters before a side-street.
# 7.	It is not 5 meters after a side-street.
# The street will be represented as a string, where each character describes a section of the street 5 meters in length. So the first character describes the first 5 meters of the street, the second character describes the next 5 meters and so on. street will use 'D' for driveway, 'B' for bus stop, 'S' for side-street and '-' for all other sections of the street. A position is directly in front of an object if it has the same index as the object in street. A position is before an object if its index is lower than the index of the object in street. Finally, a position is after an object if its index is higher than the index of the object in street.
# Given the street return the total number of possible parking spaces on that street.
# Definition
#
# Class:
# StreetParking
# Method:
# freeParks
# Parameters:
# string
# Returns:
# integer
# Method signature:
# def freeParks(self, street):

#Gendo90 has submitted the 250-point problem for 75.00 points
#Successful on ~fifth try, first had the wrong error (KeyError vs
#IndexError) and then missed that the indices could "wrap around" if negative

#probably an easier way to do this using regular expressions
class StreetParking(object):
    def freeParks(self, street):
        open_spots = 0
        #remove driveways
        street.replace("D", "X")
        street = [item for item in street]
        #print(street)
        #remove bus stops
        for i, item in enumerate(street):
            if(item=="B"):
                street[i] = "X"
                earlier = True
                try:
                    if(i-1>=0):
                        street[i-1]="X"
                    else:
                        earlier=False
                except IndexError:
                    earlier=False
                if(earlier):
                    try:
                        a = street[i-2]
                        if(a!="S"):
                            street[i-2] = "X"
                    except IndexError:
                        pass
            elif(item=="S"):
                try:
                    if(i-1>=0):
                        street[i-1]="X"
                except IndexError:
                    pass
                try:
                    if(street[i+1]!="S"):
                        street[i+1]="X"
                except IndexError:
                    pass

        open_spots = len([spot for spot in street if spot=="-"])

        return open_spots


test = StreetParking()

print(test.freeParks("B--"))
