#Problem Statement
#    
#When a widget breaks, it is sent to the widget repair shop, which is capable of repairing at most numPerDay widgets per day. Given a record of the number of widgets that arrive at the shop each morning, your task is to determine how many days the shop must operate to repair all the widgets, not counting any days the shop spends entirely idle.
#For example, suppose the shop is capable of repairing at most 8 widgets per day, and over a stretch of 5 days, it receives 10, 0, 0, 4, and 20 widgets, respectively. The shop would operate on days 1 and 2, sit idle on day 3, and operate again on days 4 through 7. In total, the shop would operate for 6 days to repair all the widgets.
#Create a class WidgetRepairs containing a method days that takes a sequence of arrival counts arrivals (of type tuple (integer)) and an integer numPerDay, and calculates the number of days of operation.
#Definition
#    
#Class:
#WidgetRepairs
#Method:
#days
#Parameters:
#tuple (integer), integer
#Returns:
#integer
#Method signature:
#def days(self, arrivals, numPerDay):

#Gendo90 has submitted the 250-point problem for 229.75 points
#Successful on first try! Took around 10 minutes

class WidgetRepairs(object):
    def days(self, arrivals, numPerDay):
        days_req = 0
        slated = 0
        for i, today in enumerate(arrivals):
            slated += today
            if(slated>0):
                days_req += 1
                slated = max(0, slated-numPerDay)

        while(slated>0):
            days_req += 1
            slated = max(0, slated-numPerDay)

        return days_req

test = WidgetRepairs()

print(test.days((100, 100), 10))
