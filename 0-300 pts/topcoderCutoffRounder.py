# Problem Statement
#
# Often, when we round a real valued number to an integer, we round up if the fractional part is 0.5 or greater, and down if the fractional part is less than 0.5. In this problem, you are to write a method round, which takes a real valued number as a string, num, and a cutoff as a string, cutoff. cutoff will be formatted exactly as "0.####", where each '#' represents a digit ('0'-'9'). At least one of the digits to the right of the decimal point in cutoff will be non-zero. Your task is to round num up if its fractional part is greater than cutoff, and down otherwise, and return the result as an integer. To avoid issues with double imprecision, the fractional part of num will not be exactly equal to cutoff  Hence, the traditional rounding method described in the opening sentence would be represented by cutoff = "0.5000"
# Definition
#
# Class:
# CutoffRounder
# Method:
# round
# Parameters:
# string, string
# Returns:
# integer
# Method signature:
# def round(self, num, cutoff):

#Gendo90 has submitted the 300-point problem for 206.51 points
#Successful on first try!
#Learned about "float" function!

class CutoffRounder(object):
    def round(self, num, cutoff):
        if("." in num):
            num_parts = num.split(".")
            num_parts[1]= "0."+num_parts[1]
            comp_val = "0."+cutoff.split(".")[1]
            if(float(comp_val)<float(num_parts[1])):
                if(num_parts[0]):
                    return int(num_parts[0])+1
                else:
                    return 1
            else:
                if(num_parts[0]):
                    return int(num_parts[0])
                else:
                    return 0
        else:
            return int(num)


test = CutoffRounder()

print(test.round("135",
"0.0001"))
