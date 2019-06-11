# Problem Statement
#
# The digits 3 and 9 share an interesting property. If you take any multiple of 3 and sum its digits, you get another multiple of 3. For example, 118*3 = 354 and 3+5+4 = 12, which is a multiple of 3. Similarly, if you take any multiple of 9 and sum its digits, you get another multiple of 9. For example, 75*9 = 675 and 6+7+5 = 18, which is a multiple of 9. Call any digit for which this property holds interesting, except for 0 and 1, for which the property holds trivially.
# A digit that is interesting in one base is not necessarily interesting in another base. For example, 3 is interesting in base 10 but uninteresting in base 5. Given an integer base, your task is to return all the interesting digits for that base in increasing order. To determine whether a particular digit is interesting or not, you need not consider all multiples of the digit. You can be certain that, if the property holds for all multiples of the digit with fewer than four digits, then it also holds for multiples with more digits. For example, in base 10, you would not need to consider any multiples greater than 999.
# Definition
#
# Class:
# InterestingDigits
# Method:
# digits
# Parameters:
# integer
# Returns:
# tuple (integer)
# Method signature:
# def digits(self, base):

# Gendo90 has submitted the 500-point problem for 272.43 points
# Successful on first try!
class InterestingDigits(object):
    def isInteresting(self, num, currentMax):
        total_added = sum(int(item) for item in currentMax)
        if(total_added%num!=0):
            return False
        else:
            return True

    def calcCurrentMax(self, newTotal, base):
        current_max = []
        for i in range(0, 3):
            newerTotal = newTotal-(base**i-1)
            if(newerTotal>0):
                current_max.insert(0, str(base-1))
                newTotal = newerTotal
            else:
                current_max.insert(0, str(0))
        return current_max

    def digits(self, base):
        # current_max = []
        # value = 1
        inter_digits = [n for n in range(2, base)]
        for possible_inter in range(2, base):
            value = 1
            current_max = [str(value*possible_inter)]
            while(len(current_max)<4):
                if(not self.isInteresting(possible_inter, current_max)):
                    inter_digits[possible_inter-2] = 0
                    break
                else:
                    value+=1
                    newTotal = value*possible_inter
                    if(newTotal>(base**3)):
                        break
                    current_max = self.calcCurrentMax(newTotal, base)

        output = [a for a in inter_digits if a!=0]
        return tuple(output)


test = InterestingDigits()

print(test.digits(10))
