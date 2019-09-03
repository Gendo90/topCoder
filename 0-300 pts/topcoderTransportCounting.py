# Problem Statement
#
# You are studying public transportation, and you want to know how many buses are going down a particular one-way street every minute. You are driving along the street by car, and counting the buses you meet or overtake. After some time, you stop counting and report the result. In this problem, you may assume that the street is a straight line, and that your car and all of the buses can only go along this line in the same direction.  You will be given an integer, speed, giving your speed in meters per minute. You will also be given a tuple (integer) positions, specifying how far ahead of you each of the buses is in meters at time 0, and a tuple (integer) velocities, specifying the velocities of the buses in meters per minute. The ith element of velocities and the ith element of positions specify the velocity and position of the ith bus, respectively. Finally, an integer, time, tells you how many minutes you should count the buses you pass for.  You should return the number of buses you will overtake or meet during time minutes. If you meet one or several buses at the first or at the final moment, count them also.
# Definition
#
# Class:
# TransportCounting
# Method:
# countBuses
# Parameters:
# integer, tuple (integer), tuple (integer), integer
# Returns:
# integer
# Method signature:
# def countBuses(self, speed, positions, velocities, time):

#Gendo90 has submitted the 250-point problem for 145.94 points
#Successful on second try - had to change a for loop into a while loop due to
#modifying the "together" array
class TransportCounting(object):
    def countBuses(self, speed, positions, velocities, time):
        curr_position = 0
        orig_len = len(positions)
        together = [[p, v] for p, v in zip(positions, velocities) if (p!=0)]
        total_overtaken = orig_len-len(together)

        while(time>0):
            curr_position+=speed
            i=0
            while(i<len(together)):
                [pos, v] = together[i]
                pos+=v
                together[i] = [pos, v]
                if(pos<=curr_position):
                    total_overtaken+=1
                    print(curr_position, together.pop(i))
                    i-=1
                i+=1
            time-=1

        return total_overtaken


test = TransportCounting()

print(test.countBuses(716, (454, 537, 44, 665, 438, 475, 897, 698, 828, 79, 233, 101), (919, 887, 572, 65, 704, 223, 306, 912, 979, 141, 337, 117), 753))
