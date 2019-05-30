# Problem Statement
#
# There are numMales males and numFemales females arranged in a circle. Starting from a given point, you count clockwise and remove the K'th person from the circle (where K=1 is the person at the current point, K=2 is the next person in the clockwise direction, etc...). After removing that person, the next person in the clockwise direction becomes the new starting point. After repeating this procedure numFemales times, there are no females left in the circle.
# Given numMales, numFemales and K, your task is to return what the initial arrangement of people in the circle must have been, starting from the starting point and in clockwise order.
# For example, if there are 5 males and 3 females and you remove every second person, your return String will be "MFMFMFMM".
# Definition
#
# Class:
# PeopleCircle
# Method:
# order
# Parameters:
# integer, integer, integer
# Returns:
# string
# Method signature:
# def order(self, numMales, numFemales, K):


# Gendo90 has submitted the 600-point problem for 197.02 points
# Successful on first try! Just took a while!
# Getting a little better...
class PeopleCircle(object):
    def order(self, numMales, numFemales, K):
        total_len = numMales+numFemales
        final = "M"*(total_len)
        original = [a for a in final]
        women_left = numFemales
        saved = []
        i=1
        while(women_left>0):
            while(original):
                if(i%K==0 and original[0]!="F" and women_left):
                    original.pop(0)
                    saved.append("F")
                    women_left-=1
                elif(i%K==0 and original[0]=="F" and women_left):
                    original.pop(0)
                    saved.append("F")
                    i-=1
                elif(original[0]=="F"):
                    saved.append(original.pop(0))
                    i-=1
                else:
                    saved.append(original.pop(0))
                i+=1
            #i=1
            original = saved[:]
            saved = []

        return ''.join(original)

test = PeopleCircle()

print(test.order(25, 25, 1000))
