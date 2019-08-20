# Problem Statement
#
# Consider a sequence {x0, x1, x2, ...}. A relation that defines some term xn in terms of previous terms is called a recurrence relation. A linear recurrence relation is one where the recurrence is of the form xn = ck-1xn-1 + ck-2xn-2 + ... + c0xn-k, where all the ci are real-valued constants, k is the length of the recurrence relation, and n is an arbitrary positive integer which is greater than or equal to k.
# You will be given a tuple (integer) coefficients, indicating, in order, c0, c1, ..., ck-1. You will also be given a tuple (integer) initial, giving the values of x0, x1, ..., xk-1, and an int N. Your method should return xN modulo 10.
# Note that the value of X modulo 10 equals the last digit of X if X is non-negative. However, if X is negative, this is not true; instead, X modulo 10 equals ((10 - ((-X) modulo 10)) modulo 10). For example, (-16) modulo 10 = ((10 - (16 modulo 10)) modulo 10) = (10 - 6) modulo 10 = 4.
# More specifically, if coefficients is of size k, then the recurrence relation will be
# xn = coefficients[k - 1] * xn-1 + coefficients[k - 2] * xn-2 + ... + coefficients[0] * xn-k.
# For example, if coefficients = {2,1}, initial = {9,7}, and N = 6, then our recurrence relation is xn = xn-1 + 2 * xn-2 and we have x0 = 9 and x1 = 7. Then x2 = x1 + 2 * x0 = 7 + 2 * 9 = 25, and similarly, x3 = 39, x4 = 89, x5 = 167, and x6 = 345, so your method would return (345 modulo 10) = 5.
# Definition
#
# Class:
# RecurrenceRelation
# Method:
# moduloTen
# Parameters:
# tuple (integer), tuple (integer), integer
# Returns:
# integer
# Method signature:
# def moduloTen(self, coefficients, initial, N):



# Gendo90 has submitted the 500-point problem for 150.00 points
# Successful on fourth try?

#had problems with the memory limit first because I did not cut down the
#"values" list and it exceeded the memory limit
#then the time limit after that... -> probably due to Python vs. lower-level
#languages...

class RecurrenceRelation(object):
    def moduloTen(self, coefficients, initial, N):
        if(isinstance(coefficients, int)):
            coefficients = [coefficients]
        if(isinstance(initial, int)):
            initial = [initial]
        coefficients = list(coefficients)
        num_coefficients = len(coefficients)
        curr_N = num_coefficients-1
        k = num_coefficients-1
        initial = list(initial)
        values = initial[:]
        shift = 0
        while(curr_N<N):
            next_val = 0
            for i in range(shift, shift+k+1):
                next_val+=coefficients[i-shift]*values[i]
            values.append(next_val)
            shift+=1
            if(len(values)>10*k):
                values = values[len(values)-(k+1):]
                shift=0
            # print(values, curr_N)
            curr_N+=1

        if(N<=len(initial)):
            if(initial[N]>=0):
                return initial[N]%10
            else:
                return ((10-((-initial[N])%10))%10)

        if(values[-1]>=0):
            return values[-1]%10
        else:
            return ((10-((-values[-1])%10))%10)

test = RecurrenceRelation()

print(test.moduloTen((758, -912), (678, 369), 50217))
