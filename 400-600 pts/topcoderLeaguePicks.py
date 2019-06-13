# Problem Statement
#
# You and your friends are setting up a fantasy TopCoder league, where you choose coders to be on your team and score points in the league when any one of your coders wins their room or successfully challenges somebody, etc. To be fair, a system has been developed to choose the order in which picks are distributed. It works like this: first, lots are drawn to choose your position in the league. Then the player with the first position gets first pick, the second player gets second pick, all the way until the last player picks. Then the order reverses: the last player chooses again, then the next to last player, and so on, until you reach the first player again. Then the cycle repeats: the first position chooses again, then the second, and so on.
# For example: say you were in the third position on a 6 player league. You would get the 3rd pick, then you'd wait until the 10th pick (the order would be 1,2,you,4,5,6,6,5,4,you), and then the 15th pick, and so on until there were no more coders to choose. If there were 20 total picks, then you would get pick numbers 3,10,15.
# Not wanting to miss your chance at a pick, your goal is to write a program that tells you what pick numbers you have in the order that you have them. You will receive three integers indicating your position in the league(1 being the first position), the number of friends that are in the league with you, and the number of picks that are being divvied up among the league. You will return an tuple (integer) that indicates the picks that you receive in ascending order.
# Definition
#
# Class:
# LeaguePicks
# Method:
# returnPicks
# Parameters:
# integer, integer, integer
# Returns:
# tuple (integer)
# Method signature:
# def returnPicks(self, position, friends, picks):

# Gendo90 has submitted the 500-point problem for 355.89 points
# Successful on first try!
class LeaguePicks(object):
    def returnPicks(self, position, friends, picks):
        forwards = [True if a==position else False for a in range(1, friends+1)]
        backwards = []
        total_picks = []
        going_forwards = True
        count_up = 0

        while(picks):
            if(going_forwards):
                this_pick = forwards.pop(0)
                backwards.append(this_pick)
            else:
                this_pick = backwards.pop()
                forwards.insert(0, this_pick)

            count_up+=1
            if(this_pick==True):
                total_picks.append(count_up)
            picks-=1
            if(not forwards):
                going_forwards = False
            if(not backwards):
                going_forwards = True

        # print(backwards)
        return tuple(total_picks)


test = LeaguePicks()

print(test.returnPicks(3, 6, 15))
