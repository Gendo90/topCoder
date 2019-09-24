# Problem Statement
#
# You are taking your car on a long trip and have only a limited amount of fuel. You know how many liters of fuel your car uses per hour for certain speeds and you'd like to know how far a certain amount of fuel will take you when travelling at the optimal speed.  You will be given a tuple (integer) velocities and a tuple (integer) consumptions. velocities specifies a number of velocities in kilometers per hour. The ith element of consumptions is the amount of fuel (in milliliters) the car will consume in 1 hour, if your speed is equal to the ith element of velocities. In addition, you will be given an integer fuel specifying the total amount of fuel in milliliters. Your method should return a float, equal to the maximum distance that the car can travel (in kilometers) with the given amount of fuel, and travelling at a constant velocity equal to one of the elements of velocities.
# Definition
#
# Class:
# FuelConsumption
# Method:
# maximalDistance
# Parameters:
# tuple (integer), tuple (integer), integer
# Returns:
# float
# Method signature:
# def maximalDistance(self, velocities, consumptions, fuel):


#Gendo90 has submitted the 250-point problem for 216.62 points
#Successful on first try!
class FuelConsumption(object):
    def maximalDistance(self, velocities, consumptions, fuel):
        #find the max velocity to consumption ratio under the fuel limit
        if(len(velocities)==1):
            return velocities[0]*fuel*1.0/(consumptions[0])
        together = zip(velocities, consumptions)
        ratios = [v*1.0/c for v, c in together]
        best_ratio = max(ratios)
        ind = ratios.index(best_ratio)

        return best_ratio*fuel

test = FuelConsumption()

print(test.maximalDistance((70, 80, 90, 100, 60, 110), (4000, 4000, 4000, 4000, 4000, 4000), 40000))
