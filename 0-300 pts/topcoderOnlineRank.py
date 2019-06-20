# Problem Statement
#
# Proposals arrive at our office in a sequence. We give each one a score. We then calcRanks its "rank" based on comparison with the scores of the most recent submissions. Its rank is 1 + the number of recent scores that are greater than it. So a rank of 1 is the best possible rank and indicates that no recent score was greater. A rank of 2 would mean that exactly one recent score was greater. We need software that can calcRanks the rank of each score.
# Create a class OnLineRank that contains a method calcRanks that is given k, the number of recent scores to use in each rank calculation, and tuple (integer) scores, the sequence of scores of the arriving proposals. The method should calcRanks the rank for each score and return the sum of all the ranks.
# Each rank should be calculated based on the preceding k scores. If fewer than k scores have preceded this score, base the calculation on all the preceding scores. (The first proposal is thus guaranteed a rank of 1.)
# Definition
#
# Class:
# OnLineRank
# Method:
# calcRanks
# Parameters:
# integer, tuple (integer)
# Returns:
# integer
# Method signature:
# def calcRanks(self, k, scores):

#Gendo90 has submitted the 250-point problem for 150.11 points
#Successful on second try - needed to clear up summation logic (a>item not
#a<item) and the i>=k condition and array slicing...
class OnLineRank(object):
    def calcRanks(self, k, scores):
        ranks = []
        for i, item in enumerate(scores):
            if(i>=k):
                comparison = scores[i-k:i]
            else:
                comparison = scores[0:i]
            print(i, comparison)
            this_rank = 1+sum(1 for a in comparison if a>item)
            ranks.append(this_rank)
        # print(ranks)

        return sum(ranks)



test = OnLineRank()

print(test.calcRanks(3, (100, 100, 99, 99, 98, 98, 97)))
