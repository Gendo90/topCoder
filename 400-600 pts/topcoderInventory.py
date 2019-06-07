# Problem Statement
#
# Inventory control is an important part of any business that maintains an inventory. On the one hand, businesses want to have enough of a product in stock that they can ship orders immediately. However, they do not want to have so much of a product in stock that all of their capital is tied up in that product. To deal with this, businesses often maintain a small stock, and replenish that stock as it is sold on a monthly basis. In other words, every month the business orders or produces more of a product so that it has some of the product in stock for the next month.  In this problem, a business wants to place a standing monthly order so that a certain number of items are delivered to it each month. Your task is to help the business determine how large a standing order to place. You will be given a tuple (integer), sales, representing the number of items that the business sold for each of a number of months, and are to determine how many they can expect to sell in an average month. Unfortunately, the business may have run out of items some months, so this is not as simple as just taking the average of the number of items sold each month.  You will be given a tuple (integer), daysAvailable, whose elements represent the number of days that the item was available in each of the months (elements of daysAvailable correspond to elements of sales with the same index). You should assume that, if the item was not available for a whole month, the business would have continued to sell the item at the same rate during the days of the month that it was not available as it did during the days the item was available, had sufficient stock been present. So, for example, if the business sold 5 items in the first half of a month, and then ran out, you can assume that they would have sold 10 items that month, if they had been available.  On months when the item was available for zero days, you can tell nothing about the number of items that might have sold, so you should not include these months in your calculation. Also, for simplicity, you may assume that all months have 30 days. Thus, if the item were in stock for exactly half of the month this would be represented by a 15 in daysAvailable. Furthermore, if the expected number of sales per month is not a whole number, you should round up since it is probably better to have one too many items than it is to have one too few.
# Definition
#
# Class:
# Inventory
# Method:
# monthlyOrder
# Parameters:
# tuple (integer), tuple (integer)
# Returns:
# integer
# Method signature:
# def monthlyOrder(self, sales, daysAvailable):


# Gendo90 has submitted the 500-point problem for 210.79 points
# Successful on second try - had to work out the "double imprecision" case
# missed because I used monthly_estimate=round(monthly_estimate)+1 instead of
# monthly_estimate=int(monthly_estimate)+1 to get the final value, so it did
# not work if it was rounding up and then adding one - it only needed to add one
# after truncating the first part

class Inventory(object):
    def monthlyOrder(self, sales, daysAvailable):
        if(isinstance(sales, int)):
            sales = [sales]
            daysAvailable = [daysAvailable]
        sales = [item for item in sales]
        daysAvailable = [item for item in daysAvailable]
        together = zip(sales, daysAvailable)
        # total_months = 0
        sales_per_month = []
        for i, item in enumerate(together):
            this_month_estimate = 0
            if(item[1]==0):
                continue
            else:
                this_month_estimate = (item[0])*30.0/(item[1])
                # if(this_month_estimate!=round(this_month_estimate)):
                #     this_month_estimate=round(this_month_estimate)+1
                sales_per_month.append(this_month_estimate)

        monthly_estimate = sum(sales_per_month)/len(sales_per_month)
        if(int(monthly_estimate)!=round(monthly_estimate, 9)):
            # print(round(monthly_estimate, 9))
            monthly_estimate=int(monthly_estimate)+1

        return int(monthly_estimate)


test = Inventory()

print(test.monthlyOrder((8514, 6386, 2876, 8878, 3832, 6676, 7371, 0, 3513, 9508, 3336, 1740, 2913, 7194, 8017, 6514, 3914, 6034, 3546, 647, 8034, 1703, 9470, 5021, 1921, 5717, 1599, 4858, 222, 1648, 9636, 1119, 690, 7644, 887, 9396, 8997, 2759, 9522),
(8, 25, 2, 18, 20, 20, 3, 0, 25, 12, 26, 20, 7, 9, 12, 25, 24, 2, 11, 28, 17, 8, 21, 15, 5, 22, 8, 13, 8, 12, 20, 11, 29, 26, 28, 23, 15, 19, 21)))
