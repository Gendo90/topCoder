# Problem Statement
#
# A magic square is a 3x3 array of numbers, such that the sum of each row, column, and diagonal are all the same. For example:
#
#     8 1 6
#     3 5 7
#     4 9 2
# In this example, all rows, columns, and diagonals sum to 15.
# You will be given a tuple (integer) representing the nine numbers of a magic square, listed left-to-right, top-to-bottom. However, one of these numbers will be replaced by a -1. Write a method to determine which number was removed. For example, if the 7 was removed from the magic square above, you would be given { 8, 1, 6, 3, 5, -1, 4, 9, 2 }, and your program should return 7.
# The completed magic square will consist of exactly 9 distinct positive integers.
# Definition
#
# Class:
# MagicSquare
# Method:
# missing
# Parameters:
# tuple (integer)
# Returns:
# integer
# Method signature:
# def missing(self, square):

#Gendo90 has submitted the 250-point problem for 230.40 points
#Successful on first try!

class MagicSquare(object):
    def missing(self, square):
        reshaped = [square[0:3], square[3:6], square[6:9]]
        target_num = 0
        replaced_val = 0
        for item in reshaped:
            if(-1 not in item):
                target_num = sum(item)
                break
        for item in reshaped:
            if(-1 in item):
                replaced_val = target_num-(sum(item)+1)
                return replaced_val


test = MagicSquare()

print(test.missing(()))
