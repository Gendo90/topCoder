# Problem Statement
#
# A letter-string is composed of letters ('A'-'Z','a'-'z') and dashes ('-'). The length of a letter-string is the number of characters in it not including dashes (in other words, the number of letters in the string). Given a list of letter-strings you will return the sum of their lengths.  Create a class LetterStrings that contains the method sum, which takes a tuple (string), s, and returns an integer representing the sum of the lengths of the given letter-strings.
# Definition
#
# Class:
# LetterStrings
# Method:
# sum
# Parameters:
# tuple (string)
# Returns:
# integer
# Method signature:
# def sum(self, s):

##Gendo90 has submitted the 250-point problem for 184.50 points
#Successful on first try!
class LetterStrings(object):
    def countLetters(self, word):
        output = word.split("-")
        output_size = [len(a) for a in output if a]
        return sum(output_size)

    def sum(self, s):
        if(isinstance(s, str)):
            return self.countLetters(s)
        else:
            total_count = 0
            for item in s:
                total_count+=self.countLetters(item)
            return total_count


test = LetterStrings()

print(test.sum("-----Abc"))
