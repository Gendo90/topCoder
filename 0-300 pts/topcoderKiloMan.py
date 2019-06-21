# Problem Statement
#
# You've reached one of the last bosses in the new hit 2-D side-scrolling action game, KiloMan. The boss has a large gun that can shoot projectiles at various heights. For each shot, KiloMan can either stand still or jump. If he stands still and the shot is at height 1 or 2, then he gets hit. If he jumps and the shot is at a height above 2, then he is also hit. Otherwise, he is not hit. Given the height of each shot and a sequence of jumps, how many hits will KiloMan take?
# The input tuple (integer) pattern is the pattern of heights at which the shots are being fired. Each element of pattern will be between 1 and 7, inclusive. The input string jumps is the sequence of jumps that KiloMan will attempt; 'J' means he will jump and 'S' means he will stand still. For example, if element 0 of pattern is 3 and character 0 of jumps is 'J', then KiloMan will jump right as a shot is fired at height 3 (and thus he will be hit).
# Your method should return an int representing the number of times KiloMan is hit.
# Definition
#
# Class:
# KiloMan
# Method:
# hitsTaken
# Parameters:
# tuple (integer), string
# Returns:
# integer
# Method signature:
# def hitsTaken(self, pattern, jumps):

#Gendo90 has submitted the 250-point problem for 240.22 points
#Successful on first try!
class KiloMan(object):
    def hitsTaken(self, pattern, jumps):
        times_hit = 0
        together = zip(pattern, jumps)
        for item in together:
            if(item[0]<=2 and item[1]=="S"):
                times_hit+=1
            elif(item[0]>2 and item[1]=="J"):
                times_hit+=1

        return times_hit



test = KiloMan()

print(test.hitsTaken((1,3,2,3,3,1,2,2,1), ("`JJSSSJSSJ`")))
