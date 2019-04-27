#    
#In documents, it is frequently necessary to write monetary amounts in a standard format. We have decided to format amounts as follows:
#the amount must start with '$'
#the amount should have a leading '0' if and only if it is less then 1 dollar.
#the amount must end with a decimal point and exactly 2 following digits.
#the digits to the left of the decimal point must be separated into groups of three by commas (a group of one or two digits may appear on the left).
#Create a class FormatAmt that contains a method amount that takes two int's, dollars and cents, as inputs and returns the properly formatted string.
#Definition
#    
#Class
#FormatAmt
#Method:
#amount
#Parameters:
#integer, integer
#Returns:
#string
#Method signature:
#def amount(self, dollars, cents):

#Gendo90 has submitted the 250-point problem for 75.00 points

#took like 4 tries, need to look at inserting items into a string at certain
#intervals, sure there is an easier way...
class FormatAmt(object):
    def amount(self, dollars, cents):
        #wait array
        amount = '$'
        str_dollars = str(dollars)
        com_dollars = [x for x in str_dollars]

        for i in range(-4, -len(com_dollars)-1, -3):
            com_dollars[i] = com_dollars[i] + ","

        amount += ''.join(com_dollars) + '.'
        if(cents<10):
            amount += '0'+str(cents)
        else:
            amount += str(cents)

        return amount

test = FormatAmt()

print(test.amount(1000, 1))
