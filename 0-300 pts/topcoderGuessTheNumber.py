import random
#Problem Statement
#    
#A popular guessing game is "Guess the number", where one person selects a number in a known range, and another person tries to guess that number. After each guess, the first person reveals whether the guess was correct, too high or too low.
#Pretty soon one learns the best strategy, which is to guess the middle number among those not yet ruled out. If there is no single middle number, then there are two numbers to choose from. In that case, we choose the smallest of those numbers.
#The algorithm can be described like this:
#Init lower and upper bound
#Repeat
#  x = (lower bound + upper bound)/2  (round down if necessary)
#  Make guess x
#  If x is too low, set lower bound to x+1
#  If x is too high, set upper bound to x-1
#Until x is correct
#For instance, assume that the lower and upper bound initally are 1 and 9, respectively. The middle number in this range is 5. If this is "too low", the new bounds become 6 and 9. This range contains four numbers, and there is thus no single middle number. The two numbers in the middle are 7 and 8, and the smallest of these is 7, so our next guess then becomes 7.
#Create a class GuessTheNumber which contains the method noGuesses which takes an integer upper, the initial upper bound of the range (the inital lower bound is always 1), and an integer answer, the number selected by the first person. The method should return an integer representing the total number of guesses required for the second person to guess the correct number using the method described above.
#Definition
#    
#Class:
#GuessTheNumber
#Method:
#noGuesses
#Parameters:
#integer, integer
#Returns:
#integer
#Method signature:
#def noGuesses(self, upper, answer):

#Gendo90 has submitted the 250-point problem for 222.07 points
#Successful on first try!

class GuessTheNumber(object):
    def noGuesses(self, upper, answer):
        count = 1
        lower = 1
        guess = (upper+lower)//2
        while(guess!=answer):
            count += 1
            if(guess<answer):
                lower = guess+1
            else:
                upper = guess-1
            guess = (upper+lower)//2

        return count

    def noGuessesRecur(self, upper, answer, lower=1, count=1):
        guess = (upper+lower)//2
        if (guess==answer):
            return count

        if(guess<answer):
            lower = guess+1
        else:
            upper = guess-1

        count+=1
        return self.noGuessesRecur(upper, answer, lower, count)

    def stress_test(self, upper_range):

        up = random.randint(1, upper_range)
        ans = random.randint(1, up)
        while(self.noGuessesRecur(up, ans)==self.noGuesses(up, ans)):
            up = random.randint(1, upper_range)
            ans = random.randint(1, up)
            print(self.noGuessesRecur(up, ans), self.noGuesses(up, ans))
        else:
            print(self.noGuessesRecur(up, ans), self.noGuesses(up, ans))
        print('Broke here')


test = GuessTheNumber()

print(test.stress_test(100000))
