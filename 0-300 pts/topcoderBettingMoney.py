# Problem Statement
#
# You run a gambling business in which people place bets on the margin of victory in a football game. At the end of the day, the company would like to know what the day's net gain has been.  Just as in any other betting system, people place certain amounts as their bets and if they guess correctly, they get their money back plus a pre-specified percentage of their bet; otherwise they lose the money they bet.  You are given a tuple (integer), amounts, the ith element of which is the number of dollars people have placed on a victory margin of i (i = 0 refers to the first element). You are also given a tuple (integer), centsPerDollar, the ith element of which is the number of cents the company has to pay for every dollar the people bet on a victory margin of i, if the final outcome is a victory margin of i. Finally, you are given an integer, finalResult, which is the final margin of victory. You have to determine what the net gain for the day was and return the amount in cents.  For example, if amounts were {10,20,30}, it would mean that people placed $10 on a draw outcome, $20 on a victory margin of 1 and $30 on a victory margin of 2, and if centsPerDollar were {20,30,40}, it would mean the people would win 20 cents per dollar bet if the match were a draw, 30 cents per dollar if the victory margin were 1 and 40 cents per dollar if the victory margin were 2.  Suppose the final result is a victory margin of 1 (i.e., finalResult = 1). Then the people who guessed the outcome as a margin of 0 or 2 were wrong and the company receives the amounts they bet, $10+$30. However, the people who guessed that the outcome would be a margin of 1 were correct, and they receive money from the company according to the amount they bet (20 dollars) and the pre-set payoff percentage (30 cents per dollar) . This amounts to 20*30 = 600 cents. Hence, the day's net gain is 40 dollars - 600 cents = 3400 cents. You should return 3400.
# Definition
#
# Class:
# BettingMoney
# Method:
# moneyMade
# Parameters:
# tuple (integer), tuple (integer), integer
# Returns:
# integer
# Method signature:
# def moneyMade(self, amounts, centsPerDollar, finalResult):

#Gendo90 has submitted the 250-point problem for 228.56 points
#Successful on first try!

#Successful on first try!
class BettingMoney(object):
    def moneyMade(self, amounts, centsPerDollar, finalResult):
        amounts = list(amounts)
        centsPerDollar = list(centsPerDollar)
        payout_bets = amounts.pop(finalResult)
        payout_perc = centsPerDollar.pop(finalResult)
        total_payout = payout_bets*payout_perc # in cents
        total_income = sum(amounts)*100.0
        net_gain = total_income-total_payout
        return net_gain



test = BettingMoney()

print(test.moneyMade())
