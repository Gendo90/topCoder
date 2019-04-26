#Problem Statement
#    
#BigBurger Inc. wants to see if having a single person at the counter both to take orders and to serve them is feasible. At each BigBurger, customers will arrive and get in line. When they get to the head of the line they will place their order, which will be assembled and served to them. Then they will leave the BigBurger and the next person in line will be able to order.
#We need to know how long a customer may be forced to wait before he or she can place an order. Given a script that lists each customer for a typical day, we want to calculate the maximum customer waiting time. Each customer in the script is characterized by an arrival time (measured in minutes after the store opened) and a service duration (the number of minutes between ordering and getting the food).
#Create a class BigBurger that contains method maxWait that is given a tuple (integer) arrival and a tuple (integer) service describing all the customers and returns the maximum time spent by a customer between arriving and placing the order. Corresponding elements of arrival and service refer to the same customer, and they are given in the order in which they arrive at the store (arrival is in non-descending order).
#If multiple customers arrive at the same time they will all join the line at the same time, with the ones listed earlier ahead of ones appearing later in the list.
#Definition
#    
#Class:
#BigBurger
#Method:
#maxWait
#Parameters:
#tuple (integer), tuple (integer)
#Returns:
#integer
#Method signature:
#def maxWait(self, arrival, service):

#Gendo90 has submitted the 250-point problem for 122.60 points
#Successful after adding if-else statement in for loop
class BigBurger(object):
    def maxWait(self, arrival, service):
        #wait array
        time_waited = []
        curr_time = arrival[0]
        for i, arr_time in enumerate(arrival):
            if(curr_time-arr_time>=0):
                time_waited.append(curr_time-arr_time)
                curr_time += service[i]
            else:
                time_waited.append(0)
                curr_time = arr_time + service[i]
            #print(time_waited)
            #print(curr_time)

        return max(time_waited)

test = BigBurger()

print(test.maxWait((2, 10, 11), (3, 4, 3)))
