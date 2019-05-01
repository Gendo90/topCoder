#Problem Statement
#    
#Margin is defined as the percentage of the selling price of an item or group of items which is profit. For example, if an item costs $80 and is sold for $100, then there is $20 profit, or 20% margin.  You will be given a tuple (string), items, which is all of the items sold in a single transaction. Each string in items will be formatted as follows: "nnn.nn nnn.nn" (quotes for clarity), where each n is a digit between '0' and '9' inclusive. Each string will be exactly 13 characters in length. #The first number listed is the price the customer paid for the item. The second number is what the cost to the store of the item was.  You will create a class ProfitCalculator with a method percent which will calculate the percentage of margin on the transaction and return it as an integer, rounded down to the greatest integer less than the actual value.  For example, let's say you were given the following tuple (string):
#   { "012.99 008.73",
#     "099.99 050.00",
#     "123.45 101.07" }
#The total cost is $159.80. The total price is $236.43. That means $76.63 was made on this sale. This would be a 32.41128% margin. Since we are rounding down, you would return 32.
#Definition
#    
#Class:
#ProfitCalculator
#Method:
#percent
#Parameters:
#tuple (string)
#Returns:
#integer
#Method signature:
#def percent(self, items):

#Gendo90 has submitted the 300-point problem for 231.28 points

#Successful on first try!
class ProfitCalculator(object):
    def percent(self, items):
        costs = []
        sales_prices = []
        for item in items:
            costs.append(float(item[7:]))
            sales_prices.append(float(item[0:6]))

        total_cost = sum(costs)
        total_sales = sum(sales_prices)
        margin = (total_sales-total_cost)/total_sales
        margin = (margin*100)//1

        return int(margin)


test = ProfitCalculator()

print(test.percent(("012.99 008.73",
     "099.99 050.00",
     "123.45 101.07")))
