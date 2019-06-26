# Problem Statement
#
# You will be given a tuple (string) cars containing a list of strings that will participate in the Train. The Train is a string that will be built using the given strings. The building process works as follows:
# Train is initialized to the value of the 0th element of cars
# For each element of cars in order, beginning with element 1, check if some proper prefix of the current element matches some proper suffix of the Train. If so, append the element of cars to the Train, not repeating the matched prefix. If more than one proper prefix matches, take the longest. If no proper prefix matches, the current element of cars is not appended.
# A prefix of a string is a substring that starts at the beginning of the string. A proper prefix is a prefix that has positive length, and is not the entire string. A suffix of a string is a substring that terminates at the end of the string. A proper suffix is a suffix that has positive length, and is not the entire string.  Once you have built the Train, remove all but the last occurrence of each character in the Train. For example, if the Train was (quotes for clarity) "abbbcabdb" you would be left with "cadb". You will return a string of the form "n x" where, n is the length of the Train before removing all but the last occurrence of each character, and x is the string after the removal. n and x are separated by exactly one space, the return should not have any leading or trailing whitespace, and n should have no leading zeros.
#
# Definition
#
# Class:
# StringTrain
# Method:
# buildTrain
# Parameters:
# tuple (string)
# Returns:
# string
# Method signature:
# def buildTrain(self, cars):

# Gendo90 has submitted the 500-point problem for 225.34 points
# Successful on first try!
# Hard to get the first part correct with the indexing...
# Need more practice with strings, and their methods
# Need to work on custom indexing as well!
class StringTrain(object):
    def buildTrain(self, cars):
        train = cars[0]
        cars = cars[1:]
        for car in cars:
            this_car_len = len(car)
            max_prefix_len = 0
            top = min(this_car_len-1, len(train)-1)
            for i in range(0, top, 1):
                if(car.startswith(train[len(train)-1-i:])):
                    max_prefix_len = i+1
            if(max_prefix_len>0):
                train += car[max_prefix_len:]

        #remove duplicate letters
        all_letters = {}
        for letter in train:
            all_letters[letter] = True

        output_len = len(train)
        # print(train)

        rev_output = ""
        for l in train[::-1]:
            if(l in all_letters):
                rev_output+=l
                all_letters.pop(l)
        output = rev_output[::-1]

        return str(output_len) + " " + output



test = StringTrain()

print(test.buildTrain(("AAAAA","AAAAA","AAAAA")))
