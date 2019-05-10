#Problem Statement
#    
#Often employees at a company time stamp their arrivals and departures, so when the month is over the boss can check how much each employee has worked. Given the time stamps for a single employee during a single day as well as his (or her) hourly wage, calculate how much the employee has earned that day.
#The time stamps are given in the format "hh:mm:ss" (quotes for clarity only) where hh is the hour (between 00 and 23 inclusive), mm is the minute (between 00 and 59 inclusive) and ss is the second (between 00 and 59 inclusive). All these numbers have exactly two digits. The arrival time stamps are inclusive, and the departure time stamps are exclusive, so an employee arriving at 09:00:00 one day and departing 17:30:00 the same day has worked exactly 8 hours 30 minutes 0 seconds during that #interval.
#An employee working during evenings (between 18:00:00 and 23:59:59, inclusive) or nights (between 00:00:00 and 05:59:59, inclusive) gets paid one and a half times as much during that period.
#Create a class Salary containing the method howMuch which takes a tuple (string), arrival, and a tuple (string), departure, the arrival and departures times of an employee, respectively, as well an integer wage, the hourly wage (in cents). Your method should return an integer representing the total amount (in cents) the employee earned during the time he or she worked. The amount should be rounded down to the largest integer less than or equal to the actual amount. Element i in arrival #corresponds to element i in departure.
#Definition
#    
#Class:
#Salary
#Method:
#howMuch
#Parameters:
#tuple (string), tuple (string), integer
#Returns:
#integer
#Method signature:
#def howMuch(self, arrival, departure, wage):

#Gendo90 has submitted the 550-point problem for 165.00 points
#Mostly successful on second try, did not realize it was a 550 point problem, missed a few = signs in the if statements
#like for departure_split[0]>=18, departure_split[0]>=6, and departure_split[0]>=18 so it would not register if the OT was in the same hour!
class Salary(object):
    def howMuch(self, arrival, departure, wage):
        total = 0
        lower_ot = [6, 0, 0]
        upper_ot = [18, 0, 0]

        for i, start_time in enumerate(arrival):
            arrival_split = start_time.split(':')
            arrival_split = [int(item) for item in arrival_split]
            departure_split = departure[i].split(':')
            departure_split = [int(item) for item in departure_split]
            hours_worked = sum((-arrival_split[n]+departure_split[n])*(60.0**(-n)) for n in range(3))
            overtime_hours_worked=0

            for n in range(3):
                if((arrival_split[0]<6 and departure_split[0]<6) or (arrival_split[0]>=18 and (departure_split[0]<6 or departure_split[0]>=18))):
                    overtime_hours_worked+=(-arrival_split[n]+departure_split[n])*(60.0**(-n))

                if(arrival_split[0]<6 and departure_split[0]>=6):
                    overtime_hours_worked+=(lower_ot[n]-arrival_split[n])*(60.0**(-n))

                if(arrival_split[0]<18 and departure_split[0]>=18):
                    overtime_hours_worked+= (-upper_ot[n]+departure_split[n])*(60.0**(-n))


            total+=(hours_worked+0.5*overtime_hours_worked)*wage

        return int(total)


test = Salary()

print(test.howMuch(("01:26:33", "02:44:28", "04:21:58", "06:23:34", "08:43:52", "11:19:35", "15:55:03", "18:05:55", "18:42:51"), ("02:08:48", "02:56:03", "05:41:40", "07:05:11", "09:55:19", "12:43:16", "16:36:19", "18:20:30", "18:57:35"), 7308))
