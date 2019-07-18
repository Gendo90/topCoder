# Problem Statement
#
# Select two numbers between 1 and 9998, inclusive, which have the same exact group of non-zero digits, but are not the same number. For example, you could use 1234 and 4321, or 91 and 901. Now, subtract the smaller of the two numbers from the larger. Finally, pick one of the non-zero digits in the result, and remove the digit from the number. If the resulting number is less than 100, prepend enough zeros so that it has 3 digits. It turns out, that given the remaining 3 digits, one can always determine the digit removed. (See examples for clarification)
# You will be given a string leftOver, which contains the three digits left over after the above algorithm is run. You must return the digit which was removed.
# Definition
#
# Class:
# NumberGuesser
# Method:
# guess
# Parameters:
# string
# Returns:
# integer
# Method signature:
# def guess(self, leftOver):

# Gendo90 has submitted the 500-point problem for 150.00 points
# Successful on ~third try?
# Still not accepting my solution due to time constraints, there is a
# fuller version that takes even longer, but the time limit is probably an
# issue because Python is "slow"
# works on my conputer in <1.5s, and the test case repeats (test case 62 and
# 70 are both "315" but one takes too long???)

#Good job!
import time
import itertools

class NumberGuesser(object):
    def guess(self, leftOver):
        seen_num = {}
        for i in range(1, 10):
            if(int(leftOver[0])<5):
                test_str = leftOver+str(i)
                test_num = int(test_str)
            else:
                test_str = str(i)+leftOver
                test_num = int(test_str)
            # print(test_nm)
            seen_num[i] = {}
            for n in range(1, 9999):
                if(n in seen_num[i]):
                    continue
                str_of_num = str(n)
                perm_arr = [a for a in itertools.permutations(str_of_num)]
                for l in range(len(perm_arr)):
                    this_perm = "".join(perm_arr[l])
                    this_perm_num = int(this_perm)
                    seen_num[i][this_perm_num] = True
                    for k in range(l+1, len(perm_arr)):
                        check_perm = "".join(perm_arr[k])
                        check_perm_num = int(check_perm)
                        seen_num[i][check_perm_num] = True
                        if(check_perm_num<1000 and this_perm_num<1000):
                            continue
                        if(this_perm_num>check_perm_num):
                            checker = this_perm_num-check_perm_num
                        else:
                            checker = check_perm_num-this_perm_num
                        if(checker==test_num):
                            return i



test = NumberGuesser()
a = time.clock()
print(test.guess("315"))
b = time.clock()
print(b-a)
