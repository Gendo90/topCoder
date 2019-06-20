# Problem Statement
#
# The dinky is a small fish that breeds monogamously and regularly. Within days of its birth, the male of the species seeks out a mate and bonds with her for life, never dallying with another. At the end of every month, the couple issues exactly two offspring, of which one is a boy and the other a girl. Each of these, in turn, goes off on its amorous quest. Inbreeding is not uncommon in the confines of a fish tank, so a pair of cousins or even siblings may end up mating. If there are more females than males, the excess number who cannot secure a mate will not give birth in that month.
# Despite their diminutive dimensions and peaceful nature, a population of dinkies must not be allowed to multiply ad infinitum. Experts recommend that one allot at least half a liter of water per dinky fish. Anything less than that, and the tank is said to be crowded. The solution is either to buy a larger tank or to catch some dinkies for breakfast.
# Given the volume of a tank in liters, the number of male dinkies currently inhabiting the tank, and the number of females present, you are to calculate the number of months that can elapse before the tank becomes crowded. Bear in mind that all couples reproduce simultaneously at the end of every month. If the input values are such that the tank is already crowded, the correct answer is 0. If the tank will become crowded at the end of the first month, the answer is 1.
# Definition
#
# Class:
# DinkyFish
# Method:
# monthsUntilCrowded
# Parameters:
# integer, integer, integer
# Returns:
# integer
# Method signature:
# def monthsUntilCrowded(self, tankVolume, maleNum, femaleNum):
#
#Gendo90 has submitted the 250-point problem for 226.51 points
#Successful on first try - but needed to get the corner case of there are
#EXACTLY enough dinkies to fill the tank (e.g. 20 dinkies in 10 L) because
#that is still valid, so numFish<=tankVolume*2, not numFish<tankVolume*2
class DinkyFish(object):
    def monthsUntilCrowded(self, tankVolume, maleNum, femaleNum):
        months = 0
        numFish=maleNum+femaleNum
        while(numFish<=tankVolume*2):
            total_couples = min(femaleNum, maleNum)
            femaleNum+=total_couples
            maleNum+=total_couples
            numFish=maleNum+femaleNum
            months+=1

        return months



test = DinkyFish()

print(test.monthsUntilCrowded(5, 6, 4))
