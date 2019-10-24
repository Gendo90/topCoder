# Problem Statement
#
# Your printer has been infected by a virus and is printing gibberish. After staring at several printed pages for a while, you realize that it is printing every line inside-out. In other words, the left half of each line is being printed starting in the middle of the page and proceeding out toward the left margin. Similarly, the right half of each line is being printed starting at the right margin and proceeding in toward the middle of the page. For example, the line
#     THIS LINE IS GIBBERISH
# is being printed as
#     I ENIL SIHTHSIREBBIG S
# Your task is to unscramble a string line from its printed form back into its original order. You can assume that line contains an even number of characters.
# Definition
#
# Class:
# InsideOut
# Method:
# unscramble
# Parameters:
# string
# Returns:
# string
# Method signature:
# def unscramble(self, line):


#Gendo90 has submitted the 250-point problem for 221.38 points
#Successful on first try!
#A little tricky to get the mid-1 part (because the array index starts at 0)
class InsideOut(object):
    def unscramble(self, line):
        line_arr = [a for a in line]
        mid = len(line)//2
        print(mid)
        output = line_arr[mid-1::-1] + line_arr[:mid-1:-1]

        return "".join(output)

test = InsideOut()

#workaround that is good to know about!
print(test.unscramble("I ENIL SIHTHSIREBBIG S"))
# print(test.unscramble(tuple(1), 20))
