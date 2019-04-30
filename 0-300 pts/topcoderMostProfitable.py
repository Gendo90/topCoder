#Problem Statement
#    
#When selling goods, it is important to know exactly how much it costs to acquire each item. A number of distributed costs, such as marketing often make this difficult, but not impossible. If a business can figure out how much an item costs, with some accuracy, then it can easily calculate the profit margins for the item. This information, combined with sales figures, can be used to determine which items are the most important to a business. In this problem you will be given the costs, prices, #and number of sales for a number of items. Each element of costs represents the total costs accrued from selling a single item. The corresponding elements (ones with the same index) of prices and sales represent the prices at which single items are sold, and the number of sales of each item that have occurred in some time period, respectively. You are to return the name of the item (the corresponding element of items) that provides the business with the most profits. If there is a tie for the #most profitable item, return the one that comes earliest in items (lowest index). If no item provides the business with positive profits you should return the empty string.
#Definition
#    
#Class:
#MostProfitable
#Method:
#bestItem
#Parameters:
#tuple (integer), tuple (integer), tuple (integer), tuple (string)
#Returns:
#string
#Method signature:
#def bestItem(self, costs, prices, sales, items):

#Gendo90 has submitted the 250-point problem for 193.59 points

#Successful on second try - missed the equals sign for top_item, because
#I thought you would return 0 if that is the 'profit', but on the upside I
#know how to read if the examples fail in a batch test now!
class MostProfitable(object):
    def bestItem(self, costs, prices, sales, items):
        profits = []
        for i, item in enumerate(items):
            item_profit = (prices[i]-costs[i])*sales[i]
            profits.append(item_profit)

        top_item = max(profits)
        if top_item <= 0:
            return ""
        else:
            ind = profits.index(top_item)
            return str(items[ind])



test = MostProfitable()

print(test.bestItem())
