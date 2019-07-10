# Problem Statement
#
# The cardinality of a binary number is given as the total number of "ones" it contains. For example, the cardinality of binary 10100 (decimal 20) is 2, because there are 2 "ones". The cardinality of binary 11110 (decimal 30) is 4, because there are 4 "ones".
# Given a tuple (integer) of decimal numbers arrange them in ascending order of binary cardinality and return this arranged tuple (integer). If two numbers have the same binary cardinality, then the smaller number must come first in the arranged tuple (integer).
# Definition
#
# Class:
# BinaryCardinality
# Method:
# arrange
# Parameters:
# tuple (integer)
# Returns:
# tuple (integer)
# Method signature:
# def arrange(self, numbers):

# Gendo90 has submitted the 500-point problem for 282.89 points
# Successful on first try! Building up stamina, and learning more about
# binary problems (other number types)

class BinaryCardinality(object):
    def secondKey(self, item):
        return item[1]

    def arrange(self, numbers):
        if(isinstance(numbers, int)):
            return (numbers)
        bin_array = [(i, bin(a)[2:]) for i, a in enumerate(numbers)]
        cardinality = [(a[0], a[1].count("1")) for a in bin_array]
        cardinality.sort(key=self.secondKey)
        first_run = [(item[1], numbers[item[0]]) for item in cardinality]
        second_run = []
        card = 0
        while(first_run):
            this_run = []
            while(first_run[0][0]==card):
                this_run.append(first_run.pop(0))
                if(first_run==[]):
                    break
            this_run.sort(key=self.secondKey)
            second_run+=this_run
            card+=1

        output = [item[1] for item in second_run]

        return output


test = BinaryCardinality()

print(test.arrange((10,9,8,7,6,5,4,3,2,1)))
