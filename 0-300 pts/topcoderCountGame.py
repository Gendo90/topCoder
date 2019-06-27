# Problem Statement
#
# The Counting Game is a game played between two players. The first player starts counting at 1, and can say no more than maxAdd numbers. The second player continues counting from where the first player left off. The two players alternate, each one contributing at least one but no more than maxAdd numbers. The player who says the goal number is the winner.
# For example, if maxAdd is 3 and the goal is 20, then a game (between bad players A and B) might go like this:
# A: 1,2,3 ... B: 4,5 ... A: 6 ... B: 7,8,9 ... A: 10,11,12 ... B: 13 ... A: 14 ... B: 15,16 ... A: 17,18 ... B: 19,20
# Since player B said the goal number, she was the winner.
# There is a perfect strategy for this game. When maxAdd is 3, if you end your turn by saying 16, then no matter whether your opponent contributes 1, 2, or 3 numbers you will be able to count to 20 on your next turn. Similarly, if you end your turn by saying 12, then no matter what your opponent does you can end your next turn by saying 16, and thus win on your following turn.
# Create a class CountGame to help you play this game. It should contain a method howMany that is given maxAdd, the most numbers you may say on each turn, goal, the goal number, and next, the number that you must start counting on. The method should return how many numbers you should say. If there is no way for you to force a win, then the method should return -1.
# Definition
#
# Class:
# CountGame
# Method:
# howMany
# Parameters:
# integer, integer, integer
# Returns:
# integer
# Method signature:
# def howMany(self, maxAdd, goal, next):

#Gendo90 has submitted the 350-point problem for 248.40 points
#Successful on first try!

#dynamic programming!
class CountGame(object):
    def howMany(self, maxAdd, goal, next):
        winner_nums = list(range(goal, next-1, -maxAdd-1))
        this_count = 0

        for num in winner_nums:
            if(0<=next+maxAdd-1-num<=maxAdd-1):
                # print(num)
                return num-next+1


        return -1



test = CountGame()

print(test.howMany(4, 50, 50))
