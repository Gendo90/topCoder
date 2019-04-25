#Problem Statement

#Create a class DivisorDigits containing a method howMany which takes an integer number and returns how many digits in number divide evenly into number itself.
#Definition

#Class:
#DivisorDigits
#Method:
#howMany
#Parameters:
#integer
#Returns:
#integer
#Method signature:
#def howMany(self, number):

# Gendo90 has submitted the 250-point problem for 237.45 points
# Successful on first go! Took ~7 minutes
class DivisorDigits(object):
    def howMany(self, number):
        num_str = str(number)
        counter = 0
        for digit in num_str:
            this_dig = int(digit)
            if this_dig!=0:
                if number%this_dig==0:
                    counter += 1

        return counter

test = DivisorDigits()

print(test.howMany(12345))
